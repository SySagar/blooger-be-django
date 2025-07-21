from posts.repositories.base import AbstractPostRepository
from posts.domains.models import postEntity as PostEntity
from posts.models import Post
from uuid import UUID
from typing import List


class DjangoORMPostRepository(AbstractPostRepository):
    def create(self, post: PostEntity) -> PostEntity:
        post_obj = Post.objects.create(
            id=post.id,
            title=post.title,
            content=post.content,
            author_id=post.author_id,
            tags=post.tags,
            created_at=post.created_at,
            updated_at=post.updated_at,
        )
        return PostEntity(
            id=post_obj.id,
            title=post_obj.title,
            content=post_obj.content,
            author_id=post_obj.author_id,
            tags=post_obj.tags,
            created_at=post_obj.created_at,
            updated_at=post_obj.updated_at,
        )
    
    def get_by_id(self, post_id):
        return super().get_by_id(post_id)
    
    def list_all(self) -> List[PostEntity]:
        posts = Post.objects.all()
        return [
            PostEntity(
                id=post.id,
                title=post.title,
                content=post.content,
                author_id=post.author_id,
                tags=post.tags.split(',') if post.tags else [],
                created_at=post.created_at,
                updated_at=post.updated_at,
            ) for post in posts
        ]