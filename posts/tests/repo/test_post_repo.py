from django.test import TestCase
from uuid import uuid4
from posts.models import Post
from posts.repositories.impl import DjangoORMPostRepository
from posts.domains.models import postEntity as PostEntity
from datetime import datetime


class DjangoORMPostRepositoryTests(TestCase):

    def test_create_and_fetch_post(self):
        repo = DjangoORMPostRepository()

        domain_post = PostEntity(
            id=uuid4(),
            title="Django Title",
            content="From ORM",
            author_id=uuid4(),
            tags=["tag"],
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow()
        )

        saved = repo.create(domain_post)
        fetched = repo.get_by_id(saved.id)

        self.assertEqual(fetched.id, saved.id)
        self.assertEqual(fetched.title, "Django Title")
