import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
from .models import Message


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.group_name = "global_chatroom"

        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )

        await self.channel_layer.group_send(
            self.group_name,
            {
                "type": "info_message",
                "message": "someone joined the chat",
                "username": ""
            }
        )

        await self.accept()

    async def disconnect(self, code):
        await self.channel_layer.group_send(
            self.group_name,
            {
                "type": "info_message",
                "message": "someone left the chat",
                "username": ""
            }
        )

        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )

    async def receive(self, text_data=None, bytes_data=None):
        data = json.loads(text_data)

        await self.save_message(data['username'], data['message'])

        await self.channel_layer.group_send(
            self.group_name,
            {
                "type": "chat_message",
                "message": data['message'],
                "username": data['username']
            }
        )

    async def chat_message(self, event):
        await self.send(
            text_data=json.dumps({
                "type": "normal",
                "message": event['message'],
                "username": event['username']
            })
        )

    async def info_message(self, event):
        await self.send(
            text_data=json.dumps({
                "type": "info",
                "message": event['message'],
                "username": event['username']
            })
        )

    @sync_to_async
    def save_message(self, username, content):
        Message.objects.create(username=username, content=content)
