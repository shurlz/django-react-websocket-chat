import json
from asgiref.sync import sync_to_async
from chat.models import Messages, ChatSpace
from channels.generic.websocket import AsyncWebsocketConsumer
from chat.serializers.messages_serializer import MessageSerializer


class ChatConsumer(AsyncWebsocketConsumer):
    # when a client makes a connection request to the web socket
    async def connect(self):
        self.chat_space_id = self.scope["url_route"]["kwargs"]["chat_space_id"]
        self.chat_space_name = f"chat_{self.chat_space_id}"
        self.user = self.scope["user"]
        self.sender_id = self.user.id

        await self.channel_layer.group_add(self.chat_space_name, self.channel_name)

        await self.accept()

    # when a client disconnecte
    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.chat_space_name, self.channel_name)

    # handles when message is sent to the backend
    async def receive(self, text_data):
        message_data = json.loads(text_data)
        message = message_data["message"]
        receiver_id = message_data["receiver"]

        # Save the message to the database
        message_obj = await self.save_message(receiver_id, message)

        # Send the message to the chat_space's WebSocket
        await self.channel_layer.group_send(
            self.chat_space_name,
            {
                "type": "chat_message",
                "message": message_obj,
                "sender_id": self.sender_id,
                "receiver_id": receiver_id,
            },
        )

    async def chat_message(self, event):
        message = event["message"]
        sender_id = event["sender_id"]
        receiver_id = event["receiver_id"]

        # Send message to WebSocket
        await self.send(
            text_data=json.dumps(
                {
                    "message": message,
                    "sender_id": sender_id,
                    "receiver_id": receiver_id,
                }
            )
        )

    # save message to the database then return the created message
    @sync_to_async
    def save_message(self, receiver_id, message) -> Messages:
        chat_space_model = ChatSpace.objects.get(public_id=self.chat_space_id)
        message_obj = Messages.create_message(
            sender_id=self.sender_id,
            receiver_id=receiver_id,
            chat_space_id=chat_space_model.id,
            content=message,
        )
        serialized_message = MessageSerializer(message_obj).data
        return serialized_message
