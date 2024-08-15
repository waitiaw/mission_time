import asyncio
from channels.generic.websocket import AsyncWebsocketConsumer
import json
from datetime import datetime

class TimeConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

        while True:
            now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            await self.send(json.dumps({'time': now}))
            await asyncio.sleep(1)

    async def disconnect(self, close_code):
        pass