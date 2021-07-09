from scrapli import Scrapli

def conn_scrapli(device, connection_key):

    connection = Scrapli(**device[connection_key])
    connection.open()

    return connection