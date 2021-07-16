from scrapli import Scrapli


class conn_scrapli():
    def __init__(self, device, connection_key):
        self.device = device
        self.connection_key = connection_key

        #check for required kwargs, grab root level key if not in connection_key
        #could have some default values?
        if 'host' not in device[connection_key]:
            device[connection_key]['host'] = device.get('host', device['name'])
        if 'username' not in device[connection_key]:
            device[connection_key]['auth_username'] = device.get('username', '')
        if 'password' not in device[connection_key]:
            device[connection_key]['auth_password'] = device.get('password', '')
        if 'platform' not in device[connection_key]:
            device[connection_key]['platform'] = device.get('platform', '')

    def connect(self):
        self.connection = Scrapli(**self.device[self.connection_key])
        self.connection.open()
        return self.connection

    def close(self):
        self.connection.close()