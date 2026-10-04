"""Pydantic schemas for Official Documentation Hub & Personalized Docs API."""

from enum import Enum

from pydantic import BaseModel, Field


class DocDifficulty(str, Enum):
    """Target skill difficulty for documentation."""
    BEGINNER = "beginner"
    INTERMEDIATE = "intermediate"
    ADVANCED = "advanced"
    ALL = "all"


class DocCategoryResponse(BaseModel):
    """Category of documentation."""
    id: str = Field(..., description="Unique category slug (e.g. 'getting-started')")
    label: str = Field(..., description="Human-friendly label")
    description: str = Field(..., description="Category summary")


class DocumentItemResponse(BaseModel):
    """Individual official documentation item."""
    id: str = Field(..., description="Unique slug/id of the documentation link")
    title: str = Field(..., description="Title of the documentation guide")
    description: str = Field(..., description="Summary explanation of what the doc covers")
    url: str = Field(..., description="Direct external URL to official docs")
    category: str = Field(..., description="Category slug matching DocCategoryResponse.id")
    source: str = Field(..., description="Publishing organization or platform (e.g. 'GitHub', 'git-scm.com')")
    tags: list[str] = Field(default_factory=list, description="Searchable keyword tags")
    target_skill_level: DocDifficulty = Field(default=DocDifficulty.ALL, description="Target skill level")
    is_recommended: bool = Field(default=False, description="Flagged true if tailored to the user's skill level/context")
    recommendation_reason: str | None = Field(default=None, description="Explanation for why this doc was recommended")
    has_full_text: bool = Field(default=False, description="True when the full document can be read in-app")


class DocumentDetailResponse(DocumentItemResponse):
    """Full document detail including in-app readable markdown content."""
    content: str = Field(..., description="Full document content in markdown, renderable in-app")


class RecommendationResponse(BaseModel):
    """Personalized documentation recommendation."""
    document: DocumentItemResponse
    reason: str = Field(..., description="Why this document is recommended for this user")
    score: float = Field(..., description="Ranking score used for ordering")


class RecommendationListResponse(BaseModel):
    """Envelope for the personalized recommendations endpoint."""
    items: list[RecommendationResponse] = Field(default_factory=list)
    user_skill_level: str | None = Field(default=None)
    user_context: str | None = Field(default=None)
    basis: str = Field(
        default="skill_level",
        description="What drove the ranking: skill_level, reading_history, default, or none",
    )


class DocsCatalogResponse(BaseModel):
    """Catalog response containing categories and list of documentation items."""
    categories: list[DocCategoryResponse] = Field(default_factory=list, description="List of categories")
    items: list[DocumentItemResponse] = Field(default_factory=list, description="Documentation items")
    total_count: int = Field(..., description="Total items matching filter")
    user_skill_level: str | None = Field(default=None, description="User's assessed skill level, if authenticated")
    user_context: str | None = Field(default=None, description="User's assessed technical background, if authenticated")
    is_personalized: bool = Field(default=False, description="Whether recommendations were personalized for user")
