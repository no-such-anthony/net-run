from napalm import get_network_driver


class conn_napalm():
    def __init__(self, device, connection_key):
        self.device = device
        self.connection_key = connection_key

        #check for required kwargs, grab root level key if not in connection_key
        #could have some default values?
        if 'hostname' not in device[connection_key]:
            device[connection_key]['hostname'] = device.get('host', device['name'])
        if 'username' not in device[connection_key]:
            device[connection_key]['username'] = device.get('username', '')
        if 'password' not in device[connection_key]:
            device[connection_key]['password'] = device.get('password', '')

        self.driver = device[connection_key].pop('driver', device.get('platform',''))


    def connect(self):
        driver = get_network_driver(self.driver)
        self.connection = driver(**self.device[self.connection_key])
        self.connection.open()
        return self.connection

    def close(self):
        self.connection.close()