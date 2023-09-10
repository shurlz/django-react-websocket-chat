import shortuuid as sh

from django.db import models
from django.contrib.auth.models import User
from chat._models.base import BaseModel


""" The Idea of ChatSpace is to create something like a group chat but for just two users,
    this is created just once when the two users first initiate a conversation, 
    and the public_id is used to setup web socket unique group ID for socket messaging
"""


class ChatSpace(BaseModel):
    participants = models.ManyToManyField(User)
    public_id = models.CharField(max_length=7, editable=False, unique=True)

    def __str__(self):
        return self.public_id

    class Meta:
        managed = True
        db_table = "ChartSpace"
        verbose_name_plural = "ChartSpace"
        ordering = ["-created_at"]

    @staticmethod
    def create(user_one: User, user_two: User) -> "ChatSpace":
        default = sh.ShortUUID().random(length=6)
        chat_space = ChatSpace(public_id=default)
        chat_space.save()

        # add the two users to the newly created chatspace
        chat_space.participants.add(user_one)
        chat_space.participants.add(user_two)
        return chat_space
