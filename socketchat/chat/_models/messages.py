from django.db import models
from django.contrib.auth.models import User
from chat._models.base import BaseModel
from chat._models.chat_space import ChatSpace


class Messages(BaseModel):
    sender = models.ForeignKey(
        to=User, related_name="sender_account", on_delete=models.CASCADE
    )
    receiver = models.ForeignKey(
        to=User, related_name="receiver_account", on_delete=models.CASCADE
    )
    chat_space = models.ForeignKey(to=ChatSpace, on_delete=models.CASCADE)
    content = models.CharField(max_length=3000)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.sender.username} > {self.receiver.username} at {self.created_at}"

    class Meta:
        managed = True
        db_table = "Messages"
        verbose_name_plural = "Messages"

    def update_read_status(self) -> "Messages":
        self.is_read = True
        return self.save()

    @staticmethod
    def create_message(
        sender_id: str, receiver_id: str, content: str, chat_space_id: str
    ) -> "Messages":
        return Messages.objects.create(
            sender_id=sender_id,
            receiver_id=receiver_id,
            content=content,
            chat_space_id=chat_space_id,
        )
