from ncclient import manager

def conn_ncclient(device, connection_key):

    connection = manager.connect(**device[connection_key])

    return connection