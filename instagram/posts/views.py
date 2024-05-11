# django imports
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view, action

# app imports
from posts.services import PostService

class PostViewSet(viewsets.ViewSet):

    def create(self, request):
        data = request.data
        post = PostService().create(
            user_id=data.get('user_id'),
            content=data.get('content')
        )
        return post.id
    
    def update(self, request, pk=None):
        data = request.data
        post = PostService().modify(
            post_id=pk,
            content=data.get('content'),
        )
        return post.id

    @action(methods=["POST"], detail=True, url_path="like")
    def like(self, request, pk=None):
        if pk is None:
            Response("No id passed")
        user_id = request.query_params.get("user_id")
        like_response = PostService().like(post_id=pk, user_id = user_id)
        Response(like_response)

    @action(methods=["POST"], detail=True, url_path="dislike")
    def dislike(self, request, pk=None):
        if pk is None:
            Response("No id passed")
        user_id = request.query_params.get("user_id")
        dislike_response = PostService().dislike(post_id=pk, user_id = user_id)
        Response(dislike_response)
