def scrapli_command(device, command=None, ckwargs={}, **kwargs):

    if command:
        output = device['nc'].send_command(command, **ckwargs)
        return output.result

    return 'No command to run.'