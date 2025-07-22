from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from pydantic import ValidationError
from posts.repositories.impl import DjangoORMPostRepository
from posts.models import Post
from uuid import UUID


from posts.interfaces.schemas import CreatePostRequest, PostResponse
from posts.use_cases.create_post import CreatePostUseCase
from posts.use_cases.get_post_by_id import GetPostByIDUseCase
from posts.use_cases.list_posts import ListPostsUseCase

class CreatePostVIew(APIView):
    def post(self, request):
        try:
            data = CreatePostRequest(**request.data)
        except ValidationError as e:
            return Response(e.errors(), status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        
        use_case = CreatePostUseCase(repo=DjangoORMPostRepository())
        post = use_case.execute(
            title=data.title,
            content=data.content,
            author_id=data.author_id,
            tags=data.tags if data.tags else None
        )
        return Response(post.model_dump(), status=status.HTTP_201_CREATED)

class ListPostsView(APIView):
     def get(self, request):
        use_case = ListPostsUseCase(repo=DjangoORMPostRepository())
        posts = use_case.execute()

        # Validate each post through PostResponse
        serialized_posts = [PostResponse(**post.model_dump()).model_dump() for post in posts]

        return Response(serialized_posts, status=status.HTTP_200_OK)


class PostDetailView(APIView):
    def get(self, request, post_id):
        use_case = GetPostByIDUseCase(repo=DjangoORMPostRepository())
        try:
            post = use_case.execute(post_id)
            return Response(post.model_dump(), status=status.HTTP_200_OK)
        except Post.DoesNotExist:
            return Response({'detail': 'Post not found'}, status=status.HTTP_404_NOT_FOUND)