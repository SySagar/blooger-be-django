from django.test import TestCase
from uuid import uuid4
from datetime import datetime
from posts.use_cases.create_post import CreatePostUseCase
from posts.domains.models import postEntity as PostEntity
from posts.repositories.base import AbstractPostRepository


class FakePostRepository(AbstractPostRepository):
    def __init__(self):
        self.posts = {}

    def create(self, post: PostEntity) -> PostEntity:
        self.posts[post.id] = post
        return post

    def get_by_id(self, post_id):
        return self.posts.get(post_id)

    def list_all(self):
        return list(self.posts.values())


class CreatePostUseCaseTests(TestCase):

    def test_create_post(self):
        repo = FakePostRepository()
        use_case = CreatePostUseCase(repo=repo)

        post = use_case.execute(
            title="New Post",
            content="Content here",
            author_id=uuid4(),
            tags=["test"]
        )

        self.assertIsNotNone(post.id)
        self.assertEqual(post.title, "New Post")
        self.assertIn(post.id, repo.posts)
