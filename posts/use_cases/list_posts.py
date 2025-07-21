from typing import List
from posts.repositories.base import AbstractPostRepository
from posts.domains.models import postEntity as PostEntity


class ListPostsUseCase:
    def __init__(self, repo: AbstractPostRepository):
        self.repo = repo

    def execute(self) -> List[PostEntity]:
        return self.repo.list_all()
