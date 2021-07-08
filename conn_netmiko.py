from netmiko import ConnectHandler
from netmiko import NetmikoTimeoutException, NetmikoAuthenticationException
from netmiko.ssh_dispatcher import telnet_platforms_str
from paramiko.ssh_exception import SSHException
from socket import timeout

from copy import deepcopy

import logging
logging.getLogger('paramiko.transport').disabled = True


def conn_netmiko(device):

    ON_CONNECTION_FAIL_TRY_TELNET = True
    ON_AUTH_FAIL_TRY_ALT_CREDS = True

    MAX_LOOP = 1 + ON_CONNECTION_FAIL_TRY_TELNET + ON_AUTH_FAIL_TRY_ALT_CREDS

    connection = None
    loop_protection = 0

    params = deepcopy(device['netmiko-ssh'])

    while not connection:

        try:
            connection = ConnectHandler(**params)
            return connection

        except (NetmikoTimeoutException, NetmikoAuthenticationException, timeout, SSHException) as e:

            # Telnet will take 1m 40s to timeout with socket.timeout
            # It failing ssh due to 'transport input telnet' under vty 
            # it may produce SSHException which was hard to manage
            # as it is also ancestor of NetmikoAuthenticationException so put them 
            # altogether in single catch
            
            if isinstance(e, NetmikoTimeoutException) or \
                 isinstance(e, timeout) or \
                 'Error reading SSH protocol banner' in str(e) or \
                 'Incompatible version' in str(e):
                if not params['device_type'].endswith('_telnet') and ON_CONNECTION_FAIL_TRY_TELNET:
                    if params['device_type'].endswith('_ssh'):
                        t = params['device_type'].replace('_ssh','_telnet')
                    else:
                        t = params['device_type'] + '_telnet'

                    if t in telnet_platforms_str:
                        params['device_type'] = t
                        params['port'] = 23
                        ON_CONNECTION_FAIL_TRY_TELNET = False
                    else:
                        # no point in trying an invalid device_type
                        raise e
    
                else:
                    raise e

            elif isinstance(e, NetmikoAuthenticationException):
                if ON_AUTH_FAIL_TRY_ALT_CREDS and 'alt_creds' in device:
                    params['username'] = device['alt_creds'].get('username', '')
                    params['password'] = device['alt_creds'].get('password', '')
                    params['secret'] = device['alt_creds'].get('secret', '')
                    ON_AUTH_FAIL_TRY_ALT_CREDS = False
                else:
                    raise e

            else:
                raise e

        loop_protection += 1
        if loop_protection > MAX_LOOP:
            raise ValueError(f"Too many attempts to connect to device {device['name']}")

    return None
