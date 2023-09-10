from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.parsers import JSONParser
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from chat.serializers.user_serializer import (
    UserRequestSerializer,
    UserResponseSerializer,
)


@api_view(["POST"])
def authenticate_user(request) -> Response:
    data = JSONParser().parse(request)
    serializer = UserRequestSerializer(data=data)
    if serializer.is_valid() is False:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    username, password = serializer.data["username"], serializer.data["password"]
    try:
        # attempt to signin user
        User.objects.get(username=username)
        user = authenticate(username=username, password=password)
        if not user:
            return Response(
                {"message": "invalid login password"},
                status=status.HTTP_400_BAD_REQUEST,
            )

    except User.DoesNotExist:
        # signup user here
        user: User = User(username=username)
        user.set_password(password)
        user.save()

    token, _ = Token.objects.get_or_create(user=user)

    return Response(
        {"token": token.key, "user": UserResponseSerializer(user).data},
        status=status.HTTP_200_OK,
    )
