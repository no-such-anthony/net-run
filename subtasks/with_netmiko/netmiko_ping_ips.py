def netmiko_ping_ips(device, ips=[], command='ping {{ip}}', ckwargs={}, **kwargs):

    output = ''
    for ip in ips:
        ping_command = command.replace('{{ip}}', ip)
        output += device['nc'].send_command(ping_command, **ckwargs)
        output += '\n\n'
    return output

