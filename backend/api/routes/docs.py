"""API endpoints for Documentation Hub and personalized documentation recommendations."""

import uuid
from typing import Annotated, Any

from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from backend.api.dependencies import get_optional_current_user
from backend.core.database import get_db
from backend.models.document_view_model import DocumentView
from backend.schemas.docs import (
    DocCategoryResponse,
    DocsCatalogResponse,
    DocumentDetailResponse,
    RecommendationListResponse,
)
from backend.services.doc_service import doc_service

router = APIRouter(prefix="/docs", tags=["Documentation Hub"])


@router.get(
    "/categories",
    response_model=list[DocCategoryResponse],
    status_code=status.HTTP_200_OK,
    summary="List all documentation categories",
)
async def list_categories() -> list[DocCategoryResponse]:
    """Retrieve catalog categories for official documentation."""
    return doc_service.get_categories()


@router.get(
    "/recommendations",
    response_model=RecommendationListResponse,
    status_code=status.HTTP_200_OK,
    summary="Personalized documentation recommendations",
)
async def get_recommendations(
    current_user: Annotated[dict[str, Any] | None, Depends(get_optional_current_user)],
    db: Annotated[AsyncSession, Depends(get_db)],
    limit: Annotated[int, Query(ge=1, le=20, description="Max recommendations to return")] = 6,
) -> RecommendationListResponse:
    """Rank documentation by the user's reading history, assessed skill level, and context.

    Guests receive evergreen featured picks so the section is never empty.
    """
    return await doc_service.get_recommendations(
        db=db,
        user_id=current_user["user_id"] if current_user else None,
        user_skill_level=current_user.get("skill_level") if current_user else None,
        user_context=current_user.get("user_context") if current_user else None,
        limit=limit,
    )


@router.get(
    "",
    response_model=DocsCatalogResponse,
    status_code=status.HTTP_200_OK,
    summary="Fetch official documentation catalog tailored to user profile",
)
async def get_documents(
    category: Annotated[str | None, Query(description="Filter by category slug")] = None,
    q: Annotated[str | None, Query(alias="query", description="Search query across documentation")] = None,
    current_user: Annotated[dict[str, Any] | None, Depends(get_optional_current_user)] = None,
) -> DocsCatalogResponse:
    """Fetch official docs catalog with personalization based on user's assessed skill level and context."""
    skill_level = current_user.get("skill_level") if current_user else None
    user_context = current_user.get("user_context") if current_user else None

    return doc_service.get_documents(
        category=category,
        query=q,
        user_skill_level=skill_level,
        user_context=user_context,
    )


@router.get(
    "/{doc_id}",
    response_model=DocumentDetailResponse,
    status_code=status.HTTP_200_OK,
    summary="Fetch the full document by id for in-app reading",
)
async def get_document_detail(doc_id: str) -> DocumentDetailResponse:
    """Return the complete markdown content of one documentation item."""
    detail = doc_service.get_document_detail(doc_id)
    if detail is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Document '{doc_id}' not found or has no full text",
        )
    return detail


@router.post(
    "/{doc_id}/view",
    status_code=status.HTTP_200_OK,
    summary="Record that the signed-in user opened a document",
)
async def record_document_view(
    doc_id: str,
    current_user: Annotated[dict[str, Any] | None, Depends(get_optional_current_user)],
    db: Annotated[AsyncSession, Depends(get_db)],
) -> dict[str, Any]:
    """Upsert one row in ``document_views``; guests are silently accepted (no-op)."""
    if not current_user:
        return {"recorded": False, "reason": "guest"}

    if doc_service.get_document_detail(doc_id) is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Document '{doc_id}' not found",
        )

    view = await db.scalar(
        select(DocumentView).where(
            DocumentView.user_id == uuid.UUID(current_user["user_id"]),
            DocumentView.doc_id == doc_id,
        )
    )
    if view is None:
        db.add(DocumentView(user_id=uuid.UUID(current_user["user_id"]), doc_id=doc_id))
    else:
        view.view_count += 1
    await db.commit()

    return {"recorded": True}
