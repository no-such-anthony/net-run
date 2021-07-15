from napalm import get_network_driver


class conn_napalm():
    def __init__(self, device, connection_key):
        self.device = device
        self.connection_key = connection_key

    def connect(self):
        driver = get_network_driver(self.device['napalm-driver'])
        self.connection = driver(**self.device[self.connection_key])
        self.connection.open()
        return self.connection

    def close(self):
        self.connection.close()