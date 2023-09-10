from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from chat.models import User, ChatSpace
from chat.serializers.default_request_serializer import DefaultIDRequestSerializer


@api_view(["POST"])
@permission_classes((IsAuthenticated,))
def chatspace(request):
    """Before two users can chat, this endpoint has to be called in order to either acquire
    the ID of their chatspace (relationship) or create a unique relationship between them
    """
    user_two_id = request.data["requested-user-id"]

    serializer = DefaultIDRequestSerializer(data={"id": user_two_id})
    if serializer.is_valid() is False:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    user_one = request.user
    try:
        user_two = User.objects.get(id=user_two_id)
    except User.DoesNotExist:
        return Response(
            {"message": "Invalid User Id"}, status=status.HTTP_400_BAD_REQUEST
        )

    # check if an instance of the two users relaltionship has been created before, then return
    instance = ChatSpace.objects.filter(participants=user_one).filter(
        participants=user_two
    )
    if instance.exists():
        return Response(
            {"chat-space-id": instance.first().public_id}, status=status.HTTP_200_OK
        )

    # create a new chatspace instance between the two users since none exists, then return
    new_instance: ChatSpace = ChatSpace.create(user_one=user_one, user_two=user_two)
    return Response(
        {"chat-space-id": new_instance.public_id}, status=status.HTTP_201_CREATED
    )
