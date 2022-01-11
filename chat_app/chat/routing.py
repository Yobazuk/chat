from django.urls import path
from .consumers import ChatConsumer


ws_urlpatterns = [
    path('ws/chatroom/', ChatConsumer.as_asgi())
]
