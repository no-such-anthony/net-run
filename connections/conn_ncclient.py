from ncclient import manager

    
class conn_ncclient():
    def __init__(self, device, connection_key):
        self.device = device
        self.connection_key = connection_key

        #check for required kwargs, grab root level key if not in connection_key
        #could have some default values?
        if 'host' not in device[connection_key]:
            device[connection_key]['host'] = device.get('host', device['name'])
        if 'username' not in device[connection_key]:
            device[connection_key]['username'] = device.get('username', '')
        if 'password' not in device[connection_key]:
            device[connection_key]['password'] = device.get('password', '')
        if 'device_params' not in device[connection_key]:
            device[connection_key]['device_params'] = { 'name': device.get('platform', '') }
        elif 'name' not in device[connection_key]['device_params']:
            device[connection_key]['device_params']['name'] = device.get('platform', '')

    def connect(self):
        self.connection = manager.connect(**self.device[self.connection_key])
        return self.connection

    def close(self):
        self.connection.close_session()