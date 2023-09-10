from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from chat.serializers.user_serializer import UserResponseSerializer
from chat.models import User


@api_view(["GET"])
@permission_classes((IsAuthenticated,))
def all_users(request):
    # return all users excluding the currently loggedin user
    users = User.objects.exclude(id=request.user.id)
    serialized_users = UserResponseSerializer(users, many=True).data

    return Response(serialized_users, status=status.HTTP_200_OK)
