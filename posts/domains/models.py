from pydantic import BaseModel, Field
from typing import List, Optional
from uuid import UUID
from datetime import datetime

# Create your models here.
class postEntity(BaseModel):
    id: UUID
    title: str = Field(..., min_length=1, max_length=255)
    content: str
    author_id: UUID
    tags: Optional[List[str]] = []
    created_at: datetime
    updated_at: datetime

    
