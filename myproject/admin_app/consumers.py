import json
from channels.generic.websocket import AsyncWebsocketConsumer
import logging

logger = logging.getLogger(__name__)

class AdminConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.group_name = "admin_orders"
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )
        await self.accept()
        logger.info("Admin WebSocket connected")

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )
        logger.info("Admin WebSocket disconnected")

    async def receive(self, text_data):
        logger.info(f"Message received: {text_data}")

    async def order_update(self, event):
        await self.send(text_data=json.dumps({
            'message': event['message']
        }))
        logger.info(f"Message sent: {event['message']}")
