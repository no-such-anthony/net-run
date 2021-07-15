from scrapli import Scrapli


class conn_scrapli():
    def __init__(self, device, connection_key):
        self.device = device
        self.connection_key = connection_key

    def connect(self):
        self.connection = Scrapli(**self.device[self.connection_key])
        self.connection.open()
        return self.connection

    def close(self):
        self.connection.close()