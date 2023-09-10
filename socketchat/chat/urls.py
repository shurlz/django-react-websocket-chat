from django.urls import path
from chat.views.auth import authenticate_user
from chat.views.chat_space import chatspace
from chat.views.users import all_users
from chat.views.messages import get_chatspace_messages, update_message_isread


urlpatterns = [
    path("auth/", authenticate_user, name="auth"),
    path("chatspace/", chatspace, name="chatspace"),
    path("all-users/", all_users, name="all-users"),
    path("messages/chatspace/", get_chatspace_messages, name="get-chatspace-messages"),
    path(
        "messages/update-status/", update_message_isread, name="update-message-status"
    ),
]
