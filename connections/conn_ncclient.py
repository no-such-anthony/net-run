from ncclient import manager

    
class conn_ncclient():
    def __init__(self, device, connection_key):
        self.device = device
        self.connection_key = connection_key

    def connect(self):
        self.connection = manager.connect(**self.device[self.connection_key])
        return self.connection

    def close(self):
        self.connection.close_session()