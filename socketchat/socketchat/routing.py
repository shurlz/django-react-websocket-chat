from django.urls import re_path
from django.urls import path
from chat.consumer import ChatConsumer

# url for the chat web socket

websocket_urlpatterns = [
    path("ws/chat/<chat_space_id>/", ChatConsumer.as_asgi()),
]
