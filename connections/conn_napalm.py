from napalm import get_network_driver

def conn_napalm(device, connection_key):

    driver = get_network_driver(device['napalm-driver'])

    connection = driver(**device[connection_key])
    connection.open()

    return connection