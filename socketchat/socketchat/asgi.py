"""
ASGI config for socketchat project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "socketchat.settings")

from channels.routing import ProtocolTypeRouter, URLRouter
from . import routing as chat_routing
from socketchat.middlewares import TokenAuthMiddleWare


application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),
        "websocket": TokenAuthMiddleWare(URLRouter(chat_routing.websocket_urlpatterns)),
    }
)
