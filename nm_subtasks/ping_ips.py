def ping_ips(device, ips=[], multi_ping=(), ckwargs={}, **kwargs):

    output = ''
    for ip in ips:
        multi_ping[2][0] = f'{ip}'
        output += device['netmiko'].send_multiline(multi_ping, **ckwargs)
        output += '\n\n'
    return output