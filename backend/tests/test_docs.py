"""Unit tests for Documentation Hub backend endpoints and personalized ranking."""

import uuid

import pytest
import pytest_asyncio
from httpx import AsyncClient, ASGITransport
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.pool import StaticPool

from backend.core.database import Base, get_db
from backend.core.jwt import create_access_token
from backend.core.security import hash_password
from backend.main import app
from backend.models.user_model import User
from backend.services.doc_service import doc_service


@pytest_asyncio.fixture
async def docs_db():
    """SQLite test DB with one verified user for view-tracking tests."""
    engine = create_async_engine(
        "sqlite+aiosqlite://",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )
    async with engine.begin() as connection:
        await connection.run_sync(Base.metadata.create_all)
    session_factory = async_sessionmaker(engine, expire_on_commit=False)
    session = session_factory()
    user = User(
        id=uuid.uuid4(),
        email="reader@example.com",
        username="reader",
        password_hash=hash_password("password-123"),
        skill_level="beginner",
        role="user",
        account_status="active",
        is_active=True,
    )
    session.add(user)
    await session.commit()

    async def override_get_db():
        yield session

    app.dependency_overrides[get_db] = override_get_db
    yield session, user
    app.dependency_overrides.clear()
    await session.close()
    await engine.dispose()


@pytest.mark.asyncio
async def test_get_doc_categories() -> None:
    """Test retrieving categories list."""
    categories = doc_service.get_categories()
    assert len(categories) == 9
    cat_ids = [c.id for c in categories]
    assert "getting-started" in cat_ids
    assert "git" in cat_ids
    assert "github" in cat_ids


@pytest.mark.asyncio
async def test_get_documents_default() -> None:
    """Test retrieving documentation without filters."""
    res = doc_service.get_documents()
    assert res.total_count == 44
    assert len(res.items) == 44
    assert res.is_personalized is False


@pytest.mark.asyncio
async def test_get_documents_category_filter() -> None:
    """Test category filtering."""
    res = doc_service.get_documents(category="git")
    assert res.total_count > 0
    assert all(item.category == "git" for item in res.items)


@pytest.mark.asyncio
async def test_get_documents_search_query() -> None:
    """Test keyword searching in title/tags."""
    res = doc_service.get_documents(query="rebase")
    assert res.total_count > 0
    titles = [item.title.lower() for item in res.items]
    assert any("rebase" in t or "history" in t for t in titles)


@pytest.mark.asyncio
async def test_get_documents_personalized_beginner() -> None:
    """Test personalization for beginner skill level."""
    res = doc_service.get_documents(user_skill_level="beginner")
    assert res.is_personalized is True
    assert res.user_skill_level == "beginner"
    # First item should be recommended for beginner
    recommended = [i for i in res.items if i.is_recommended]
    assert len(recommended) > 0
    assert "beginner" in (recommended[0].recommendation_reason or "").lower()


@pytest.mark.asyncio
async def test_get_documents_personalized_context() -> None:
    """Test personalization with user_context keywords."""
    res = doc_service.get_documents(
        user_skill_level="intermediate",
        user_context="Experienced in Python microservices, security scanning, and github-actions automation",
    )
    assert res.is_personalized is True
    recommended = [i for i in res.items if i.is_recommended]
    assert len(recommended) > 0


@pytest.mark.asyncio
async def test_api_docs_endpoint() -> None:
    """Test GET /api/v1/docs HTTP endpoint."""
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        response = await ac.get("/api/v1/docs")
        assert response.status_code == 200
        data = response.json()
        assert "items" in data
        assert "categories" in data
        assert data["total_count"] == 44


@pytest.mark.asyncio
async def test_api_docs_categories_endpoint() -> None:
    """Test GET /api/v1/docs/categories HTTP endpoint."""
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        response = await ac.get("/api/v1/docs/categories")
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
        assert len(data) == 9


@pytest.mark.asyncio
async def test_api_docs_detail_full_text() -> None:
    """Test GET /api/v1/docs/{id} returns full markdown content."""
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        response = await ac.get("/api/v1/docs/about-pull-requests")
        assert response.status_code == 200
        data = response.json()
        assert data["id"] == "about-pull-requests"
        assert data["has_full_text"] is True
        assert "pull request" in data["content"].lower()
        assert len(data["content"]) > 500


@pytest.mark.asyncio
async def test_api_docs_detail_not_found() -> None:
    """Test GET /api/v1/docs/{id} returns 404 for unknown ids."""
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        response = await ac.get("/api/v1/docs/does-not-exist")
        assert response.status_code == 404


@pytest.mark.asyncio
async def test_api_docs_recommendations_guest_default() -> None:
    """Guests get evergreen default picks with a usable reason."""
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        response = await ac.get("/api/v1/docs/recommendations")
        assert response.status_code == 200
        data = response.json()
        assert len(data["items"]) > 0
        assert data["basis"] == "default"
        first = data["items"][0]
        assert first["reason"]
        assert first["document"]["is_recommended"] is True


@pytest.mark.asyncio
async def test_api_docs_recommendations_personalized(docs_db) -> None:
    """Authenticated user with a skill level gets skill-based ranking."""
    _session, user = docs_db
    token = create_access_token(str(user.id))
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        response = await ac.get(
            "/api/v1/docs/recommendations",
            headers={"Authorization": f"Bearer {token}"},
        )
        assert response.status_code == 200
        data = response.json()
        assert data["user_skill_level"] == "beginner"
        assert data["basis"] == "skill_level"
        assert len(data["items"]) > 0


@pytest.mark.asyncio
async def test_api_docs_view_tracking_and_history_ranking(docs_db) -> None:
    """View tracking upserts and reading history drives recommendations."""
    _session, user = docs_db
    token = create_access_token(str(user.id))
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        # Record one view twice.
        for _ in range(2):
            resp = await ac.post(
                "/api/v1/docs/learn-git-branching/view",
                headers={"Authorization": f"Bearer {token}"},
            )
            assert resp.status_code == 200
            assert resp.json() == {"recorded": True}

        # Recommendations should now be history-driven and exclude the read doc.
        resp = await ac.get(
            "/api/v1/docs/recommendations",
            headers={"Authorization": f"Bearer {token}"},
        )
        assert resp.status_code == 200
        data = resp.json()
        assert data["basis"] == "reading_history"
        rec_ids = [item["document"]["id"] for item in data["items"]]
        assert "learn-git-branching" not in rec_ids
        assert len(rec_ids) > 0

        # Second view should have incremented view_count, not created a new row.
        from sqlalchemy import select

        from backend.models.document_view_model import DocumentView

        rows = (await _session.execute(select(DocumentView))).scalars().all()
        assert len(rows) == 1
        assert rows[0].view_count == 2


@pytest.mark.asyncio
async def test_api_docs_view_unknown_doc_404(docs_db) -> None:
    """Recording a view for an unknown document id returns 404."""
    _session, user = docs_db
    token = create_access_token(str(user.id))
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        response = await ac.post(
            "/api/v1/docs/no-such-doc/view",
            headers={"Authorization": f"Bearer {token}"},
        )
        assert response.status_code == 404
