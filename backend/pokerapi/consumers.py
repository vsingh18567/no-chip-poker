from channels.consumer import SyncConsumer


class GameConsumer(SyncConsumer):
    def websocket_connect(self, e):
        self.send({})
