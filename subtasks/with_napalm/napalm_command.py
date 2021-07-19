def napalm_command(device, command=None, ckwargs={}, **kwargs):

    if command:
        output = device['nc'].cli(command, **ckwargs)
    else:
        output = 'No command to run.'

    return output