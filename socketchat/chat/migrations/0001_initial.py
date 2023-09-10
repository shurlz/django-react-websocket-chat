# Generated by Django 4.2.5 on 2023-09-09 09:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="ChatSpace",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "public_id",
                    models.CharField(
                        default="3Mg8T4", editable=False, max_length=7, unique=True
                    ),
                ),
                ("participants", models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                "verbose_name_plural": "ChartSpace",
                "db_table": "ChartSpace",
                "ordering": ["-created_at"],
                "managed": True,
            },
        ),
        migrations.CreateModel(
            name="Messages",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("content", models.CharField(max_length=3000)),
                ("is_read", models.BooleanField(default=False)),
                (
                    "chat_space",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="chat.chatspace"
                    ),
                ),
                (
                    "receiver",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="receiver_account",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "sender",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="sender_account",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Messages",
                "db_table": "Messages",
                "managed": True,
            },
        ),
    ]