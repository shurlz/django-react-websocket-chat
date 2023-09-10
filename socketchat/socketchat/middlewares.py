from rest_framework.authtoken.models import Token
from urllib.parse import parse_qs
from channels.db import database_sync_to_async
from django.http import HttpResponseForbidden


# fetching the user data through the provided token


@database_sync_to_async
def return_user(token_string):
    try:
        user = Token.objects.get(key=token_string).user
        return user
    except:
        return None


# authentication middleware class to be used during web socket requests


class TokenAuthMiddleWare:
    def __init__(self, app):
        self.app = app

    async def __call__(self, scope, receive, send):
        try:
            query_string = scope["query_string"]
            query_params = query_string.decode()
            query_dict = parse_qs(query_params)
            token = query_dict["token"][0]
        except:
            return HttpResponseForbidden("Please provide a token")

        user = await return_user(token)
        if user is None:
            return HttpResponseForbidden("Invalid login token")
        scope["user"] = user
        return await self.app(scope, receive, send)
