from connections.conn_netmiko import conn_netmiko
from connections.conn_scrapli import conn_scrapli
from connections.conn_ncclient import conn_ncclient
from connections.conn_napalm import conn_napalm


connectors = { 'scrapli': conn_scrapli,
               'netmiko': conn_netmiko,
               'ncclient': conn_ncclient,
               'napalm': conn_napalm,
               }
