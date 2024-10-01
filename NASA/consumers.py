from channels.generic.websocket import AsyncWebsocketConsumer
import json

class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Add this WebSocket connection to the group
        print("connected")
        await self.channel_layer.group_add(
            "notifications_group",  # Name of the group
            self.channel_name           # Channel name for this connection
        )
        await self.accept()

    async def disconnect(self, close_code):
        # Remove the WebSocket connection from the group
        await self.channel_layer.group_discard(
            "notifications_group",
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data.get('message')

        # Broadcast the message to the group
        await self.channel_layer.group_send(
            "notifications_group",
            {
                'type': 'chat_message',  # Custom event type
                'message': message
            }
        )

    # This method will handle messages sent to the group
    async def chat_message(self, event):
        message = event['message']

        # Send the message to the WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))
