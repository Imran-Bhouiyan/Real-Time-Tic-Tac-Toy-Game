from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
import json



class TicToyeAsync(WebsocketConsumer):
    def connect(self):
        print("socket is connected")
        self.room_name = 'tic_toe'
        self.room_group_name = 'game'
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.accept()

        
    def disconnect(self):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )
        
    def receive(self , text_data):
        print(text_data)
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,{
                'type' : 'run_game',
                'payload' : text_data
            }
        )
        
    
    def run_game(self , event):
        data = event['payload']
        data = json.loads(data)

        self.send(text_data= json.dumps({
            'payload' : data['data']
        }))        
        



# import asyncio
# from channels.generic.websocket import JsonWebsocketConsumer , AsyncJsonWebsocketConsumer
# from asgiref.sync import async_to_sync ,sync_to_async
# from channels.db import database_sync_to_async

# from channels.layers import get_channel_layer

# class TicToyeAsync(AsyncJsonWebsocketConsumer):

#     async def connect(self ):
#         print("socket is connected")
#         self.room_name = 'tic_toe'
#         self.room_group_name = 'game'
#         await self.channel_layer.group_add(
#             self.room_group_name,
#             self.channel_name
#         )
#         await self.accept()

#     async def disconnect(self):
#         async_to_sync(self.channel_layer.group_discard)(
#             self.room_group_name,
#             self.channel_name
#         )
        
#     def receive(self , text_data):
#         print(text_data)
#         async_to_sync(self.channel_layer.group_send)(
#             self.room_group_name,{
#                 'type' : 'run_game',
#                 'payload' : text_data
#             }
#         )
        
    
#     def run_game(self , event):
#         data = event['payload']
#         data = json.loads(data)

#         self.send(text_data= json.dumps({
#             'payload' : data['data']
#         }))         
        

