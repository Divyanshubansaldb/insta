# django imports
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers, status

# app imports
from users.models import User

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            "id",
            "username",   
        ]