async def basic_command(device, command=None, ckwargs={}, **kwargs):

    if command:
        output = await device['nc'].send_command(command, **ckwargs)
        return output.result

    return 'No command to run.'