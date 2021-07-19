def netmiko_config(device, configuration=None, **kwargs):

    if configuration:
        output = device['nc'].send_config_set(configuration)
    else:
        output = "No configuration to send."
    return output