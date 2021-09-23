import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from .models import Message
from django.utils.crypto import get_random_string
from django.contrib.auth import get_user_model
from datetime import datetime



User = get_user_model()


class ChatConsumer(WebsocketConsumer):


    
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
       
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

  
    def receive(self, text_data):
        username = self.scope["user"].username
        name = self.scope['user'].username
        print(self, text_data)
        now = datetime.now()
        current_time = now.strftime("%H:%M")
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        frontendMessage = (username + ' [' + current_time + '] ' + ':\n' + message)
        new_message = Message.objects.create(content=message, author=self.scope['user'], message_id=get_random_string(length=20))
     
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {   
                'type': 'chat_message',
                'message': frontendMessage,
                'author': username
            }
        )

  
    def chat_message(self, event):
        username = self.scope["user"].username
        name = self.scope["user"].username
        message = event['message']
      
        self.send(text_data=json.dumps({
            'message': message,
            "username": username,
            "name": name
        }))