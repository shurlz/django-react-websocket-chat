from rest_framework import serializers
from chat.models import Messages
from chat.serializers.user_serializer import UserResponseSerializer


class MessageSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)
    chat_space = serializers.CharField(read_only=True)
    sender = UserResponseSerializer(many=False)
    receiver = UserResponseSerializer(many=False)

    class Meta:
        model = Messages
        fields = "__all__"
