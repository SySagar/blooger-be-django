from abc import ABC, abstractmethod
from uuid import UUID
from typing import List
from posts.domains.models import postEntity

class AbstractPostRepository(ABC):

    @abstractmethod
    def create(self, post: postEntity) -> postEntity:
        """Create a new post."""
        pass

    @abstractmethod
    def get_by_id(self, post_id: UUID) -> postEntity:
        """Retrieve a post by ID"""
        pass

    @abstractmethod
    def list_all(self) -> List[postEntity]:
        """List all posts"""
        pass