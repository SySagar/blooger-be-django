from uuid import UUID
from posts.repositories.base import AbstractPostRepository
from posts.domains.models import postEntity as PostEntity


class GetPostByIDUseCase:
    def __init__(self, repo: AbstractPostRepository):
        self.repo = repo

    def execute(self, post_id: UUID) -> PostEntity:
        return self.repo.get_by_id(post_id)
