from channels.generic.websocket import WebsocketConsumer
import json

class WSconsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        self.send(json.dumps({'message': 'hemlo'}))
