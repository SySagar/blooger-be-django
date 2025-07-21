from pydantic import BaseModel, Field
from typing import List, Optional
from uuid import UUID
from datetime import datetime


class CreatePostRequest(BaseModel):
    title: str = Field(..., min_length=1, max_length=255)
    content: str
    author_id: UUID
    tags: Optional[List[str]] = []

class PostResponse(BaseModel):
    id: UUID
    title: str
    content: str
    author_id: UUID
    tags: List[str]
    created_at: datetime
    updated_at: datetime