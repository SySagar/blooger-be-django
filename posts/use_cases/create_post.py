from typing import Optional, List
from uuid import UUID, uuid4
from datetime import datetime

from posts.domains.models import postEntity
from posts.repositories.base import AbstractPostRepository

class CreatePostUseCase:
    def __init__(self, repo: AbstractPostRepository):
        self.repo = repo

    def execute(
        self,
        title: str,
        content: str,
        author_id: UUID,
        tags: Optional[List[str]] = None,
    ) -> postEntity:
        now = datetime.utcnow()
        post = postEntity(
            id=uuid4(),
            title=title,
            content=content,
            author_id=author_id,
            tags=tags or [],
            created_at=now,
            updated_at=now,
        )
        return self.repo.create(post)