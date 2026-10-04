"""DocumentView model: per-user reading history for the Documentation Hub."""

import uuid

from sqlalchemy import DateTime, ForeignKey, String, UniqueConstraint, Uuid, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.core.database import Base


class DocumentView(Base):
    """One row per user per documentation item the user opened in-app.

    Aggregates across visits; used to rank personalized doc recommendations.
    """

    __tablename__ = "document_views"
    __table_args__ = (
        UniqueConstraint("user_id", "doc_id", name="uq_document_views_user_doc"),
    )

    id: Mapped[uuid.UUID] = mapped_column(Uuid(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id: Mapped[uuid.UUID] = mapped_column(
        Uuid(as_uuid=True),
        ForeignKey("users.id", ondelete="CASCADE"),
        index=True,
        nullable=False,
    )
    doc_id: Mapped[str] = mapped_column(String(120), index=True, nullable=False)
    view_count: Mapped[int] = mapped_column(default=1, nullable=False)
    last_viewed_at: Mapped[object] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )
    first_viewed_at: Mapped[object] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )

    user = relationship("User", back_populates="document_views")
