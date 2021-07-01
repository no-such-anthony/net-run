def basic_command(device, command=None, ckwargs={}, **kwargs):

    if command:
        output = device['nc'].send_command(command, **ckwargs)
    else:
        output = 'No command to run.'

    return output