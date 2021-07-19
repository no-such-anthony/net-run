def ncclient_get_config(device, source='running', **kwargs):
    output = device['nc'].get_config(source=source).data_xml
    return output