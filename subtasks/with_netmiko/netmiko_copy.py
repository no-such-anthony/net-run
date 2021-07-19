def netmiko_copy(device, source='', destination='', ckwargs={}, **kwargs):

    # Example of a copy subtask

    if source and destination:
        command = f'copy {source} {destination}'

        # For Cisco as long "file prompt" is either alert or noisy this should work
        # if "file prompt" is quiet try just the send_command without the expect_string.

        # For SCP, use the Netmiko file_transfer command instead

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

        if '%Error' not in output:
            output = 'Successful copy.\n\n' + output
        else:
            output = 'Failed to copy.\n\n' + output
    else:
        output = 'Copying needs both a source and desintation.'

    #print(output)


    return output
