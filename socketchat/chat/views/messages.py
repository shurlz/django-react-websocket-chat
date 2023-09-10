from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from chat.serializers.messages_serializer import MessageSerializer
from chat.models import ChatSpace, Messages
from chat.serializers.default_request_serializer import DefaultIDRequestSerializer


@api_view(["POST"])
@permission_classes((IsAuthenticated,))
def get_chatspace_messages(request):
    """Get All messages between two users, using their chatspace ID"""
    chat_space_public_id = request.data["chatspace-id"]

    serializer = DefaultIDRequestSerializer(data={"id": chat_space_public_id})
    if serializer.is_valid() is False:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    try:
        chat_space = ChatSpace.objects.get(public_id=chat_space_public_id)
    except ChatSpace.DoesNotExist:
        return Response(
            {"error": "chatspace-id invalid"}, status=status.HTTP_400_BAD_REQUEST
        )

    all_messages = Messages.objects.filter(chat_space=chat_space).all()
    serialized_messages = MessageSerializer(all_messages, many=True).data

    return Response(serialized_messages, status=status.HTTP_200_OK)


@api_view(["POST"])
@permission_classes((IsAuthenticated,))
def update_message_isread(request):
    """Used to update message is read status"""
    message_id = request.data["message-id"]

    serializer = DefaultIDRequestSerializer(data={"id": message_id})
    if serializer.is_valid() is False:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    try:
        message = Messages.objects.get(id=message_id)
    except Messages.DoesNotExist:
        return Response(
            {"error": "message does not exist"}, status=status.HTTP_400_BAD_REQUEST
        )

    updated_msg = message.update_read_status()
    serialized_message = MessageSerializer(updated_msg).data

    return Response(serialized_message, status=status.HTTP_200_OK)
