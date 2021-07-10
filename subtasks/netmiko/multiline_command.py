def multiline_command(device, command=None, ckwargs={}, **kwargs):

    if command:
        output = device['nc'].send_multiline(command, **ckwargs)
    else:
        output = 'Np multiline command to run.'

    return output