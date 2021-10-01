from rest_framework import mixins, generics
from .serializers import UserSerializer
from django.contrib.auth.models import User


class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

