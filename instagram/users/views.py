# django imports
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view, action

# app imports 
from users.models import User
from users.serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    http_method_names = ["post", "get"]

    def create(self, request, *args, **kwargs):
        User.objects.create(
            username = request.data.get('username'),
            mobile_no = request.data.get('mobile_no'),
        )
        return Response(User.id)