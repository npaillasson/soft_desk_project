from rest_framework import generics
from .serializers import UserSerializer
from rest_framework.permissions import AllowAny


class UserCreate(generics.CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserSerializer
