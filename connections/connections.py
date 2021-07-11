from connections.conn_netmiko import conn_netmiko
from connections.conn_scrapli import conn_scrapli
from connections.conn_ncclient import conn_ncclient

def get_connection(device, connection_type, connection_key):
    if connection_type == 'netmiko':
        return conn_netmiko(device, connection_key)
    elif connection_type == 'scrapli':
        return conn_scrapli(device, connection_key)
    elif connection_type == 'ncclient':
        return conn_ncclient(device, connection_key)
    return None

def close_connection(connection, connection_type):
    if connection_type == 'netmiko':
        connection.disconnect()
    elif connection_type == 'scrapi':
        connection.close()
    elif connection_type == 'ncclient':
        connection.close_session()
