def copy_command(device, source='', destination='', ckwargs={}, **kwargs):

    if source and destination:
        command = f'copy {source} {destination}'

        # For Cisco as long "file prompt" is either alert or noisy this should work
        # if "file prompt" is quiet try just the send_command without the expect_string.

        output = device['nc'].send_command_timing(command)
        if "Address or name" or "Source filename" in output:
            output += '\n'
            output += device['nc'].send_command_timing('\n')
        if "Address or name" or "Source filename" in output:
            output += '\n'
            output += device['nc'].send_command_timing('\n')
        if 'Destination filename' in output:
            output += '\n'
            output += device['nc'].send_command('\n', expect_string=r'#', **ckwargs)

    else:
        output = 'Copying needs both a source and desintation.'

    print(output)

    return output
