import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
from .models import Chat,Room
from accounts.models import User
class ChatConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        #join room
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        #Leave room
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
    # receive message from websocket
    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data['message']
        username = data['username']
        room = data['room']

        await self.save_message(username,room,message)

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'username': username,
                'message': message
            }
        )
    
    # receive message from room group
    async def chat_message(self,event):
        message = event['message']
        username = event['username']
        
        await self.send(text_data=json.dumps({
            'message': message,
            'username': username,
        }))
    
    @sync_to_async
    def save_message(self,username,room,message):
        chatRoom = Room.objects.get(name=room)
        user = User.objects.get(email=username)
        chats =Chat.objects.create(username=user,room=chatRoom,content=message)
        
        