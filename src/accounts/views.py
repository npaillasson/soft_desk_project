from django.core import exceptions
from rest_framework.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password
from rest_framework import viewsets
from .serializers import UserSerializer
from rest_framework.permissions import AllowAny
from .models import User


class UserCreate(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        try:
            validate_password(serializer.validated_data["password"])
        except exceptions.ValidationError as exception_to_return:
            exception_to_return = ", ".join(exception_to_return)
            detail = {"password": "{}".format(exception_to_return)}
            raise ValidationError(detail=detail)
        else:
            user = User.objects.create(
                username=serializer.validated_data["username"],
                email=serializer.validated_data["email"],
                first_name=serializer.validated_data["first_name"],
                last_name=serializer.validated_data["last_name"],
            )
            user.set_password(serializer.validated_data["password"])
            user.save()
