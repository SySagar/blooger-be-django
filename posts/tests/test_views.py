from rest_framework.test import APITestCase
from rest_framework import status
from uuid import uuid4
from posts.models import Post
from django.urls import reverse

class PostAPITests(APITestCase):
    def setUp(self):
        self.author_id = uuid4()
        self.post = Post.objects.create(
            id=uuid4(),
            title="Test Post",
            content="This is a test post.",
            author_id=self.author_id,
            tags=["test", "sample"]
        )

    def test_create_post(self):
        url = reverse('create_post')
        data = {
          "title": "New Post",
          "content": "This is new content.",
          "author_id": str(self.author_id),
          "tags": ["new", "blog"]  
        }
        res = self.client.post(url, data, format='json')
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Post.objects.count(), 2)
        self.assertEqual(Post.objects.last().title, "New Post")

    def test_list_posts(self):
        url = reverse('list_posts')
        res = self.client.get(url, format='json')
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data), 1)

    def test_get_post_by_id(self):
        url = reverse("post_detail", args=[str(self.post.id)])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["id"], str(self.post.id))

    def test_get_post_invalid_id(self):
        url = reverse("post_detail", args=[str(uuid4())])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)