from netmiko import ConnectHandler
from netmiko import NetmikoTimeoutException, NetmikoAuthenticationException
from netmiko.ssh_dispatcher import telnet_platforms_str
from paramiko.ssh_exception import SSHException
from socket import timeout

from copy import deepcopy

import logging
logging.getLogger('paramiko.transport').disabled = True


class conn_netmiko():
    def __init__(self, device, connection_key):
        self.device = device
        self.connection_key = connection_key
        self.connection = None

    def connect(self):
        ON_CONNECTION_FAIL_TRY_TELNET = False  # Telnet will take 1m 40s to timeout with socket.timeout
        ON_AUTH_FAIL_TRY_ALT_CREDS = False
        RETRIES_BEFORE_ALT_ATTEMPTS = 0

        MAX_LOOP = 1 + RETRIES_BEFORE_ALT_ATTEMPTS + ON_CONNECTION_FAIL_TRY_TELNET + ON_AUTH_FAIL_TRY_ALT_CREDS

        connection = None
        loop_protection = 0

        device = self.device
        params = deepcopy(device[self.connection_key])

        while not connection:

            #print(params)
            try:
                self.connection = ConnectHandler(**params)
                return self.connection

            except (NetmikoTimeoutException, NetmikoAuthenticationException, timeout, SSHException) as e:

                if loop_protection >= RETRIES_BEFORE_ALT_ATTEMPTS:

                    if ON_CONNECTION_FAIL_TRY_TELNET or ON_AUTH_FAIL_TRY_ALT_CREDS:
                    
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
                    else:
                        raise e

            loop_protection += 1

            # unlikely?  just in case MAX_LOOP ever reached
            if loop_protection > MAX_LOOP:
                raise ValueError(f"Too many attempts to connect to device {device['name']}")

        return self.connection

    def close(self):
        self.connection.disconnect()
