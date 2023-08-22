from channels.consumer import SyncConsumer,AsyncConsumer
from channels.exceptions import StopConsumer
from time import sleep
import asyncio
import json
from asgiref.sync import async_to_sync
from .models import Group
from channels.db import database_sync_to_async


class MySyncConsumer(SyncConsumer):

    def websocket_connect(self, event):
        print("WebSocket connected", event)
        group_name = self.scope['url_route']['kwargs']['groupname']
        async_to_sync(self.channel_layer.group_add)(group_name,self.channel_name)
        self.send({
            'type':'websocket.accept'
        })

    def websocket_receive(self, event):
        print("WebSocket received", event)
        group_name = self.scope['url_route']['kwargs']['groupname']
        data = json.loads(event['text'])
        group = Group.objects.get(group_name = group_name)
        group.containt = data['msg']
        group.save()
        async_to_sync(self.channel_layer.group_send)(group_name,{
            'type':'chat.message',
            'message':event['text']
        })

    def chat_message(self,event):
        self.send({
            'type':'websocket.send',
            'text':event['message']
        })

    def websocket_disconnect(self, event):
        print("WebSocket disconnected", event)
        group_name = self.scope['url_route']['kwargs']['groupname']
        async_to_sync(self.channel_layer.group_discard)(group_name,self.channel_name)
        raise StopConsumer()


class MyAsyncConsumer(AsyncConsumer):

    async def websocket_connect(self, event):
        print("WebSocket connected", event)
        group_name = self.scope['url_route']['kwargs']['groupname']
        await self.channel_layer.group_add(group_name,self.channel_name)
        await self.send({
            'type':'websocket.accept'
        })

    async def websocket_receive(self, event):
        print("WebSocket received", event)
        group_name = self.scope['url_route']['kwargs']['groupname']
        data = json.loads(event['text'])
        group = await database_sync_to_async(Group.objects.get)(group_name = group_name)
        group.containt = data['msg']
        await database_sync_to_async(group.save)()
        await self.channel_layer.group_send(group_name,{
            'type':'chat.message',
            'message':event['text']
        })

    async def chat_message(self,event):
        await self.send({
            'type':'websocket.send',
            'text':event['message']
        })

    async def websocket_disconnect(self, event):
        print("WebSocket disconnected", event)
        group_name = self.scope['url_route']['kwargs']['groupname']
        await self.channel_layer.group_discard(group_name,self.channel_name)
        raise StopConsumer()

