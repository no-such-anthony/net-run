import re
import difflib


def config_filter_cisco_ios(cfg):
    """Filter unneeded items that change from the config."""

    # Strip the header line
    header_line1_re = r"^Building configuration.*$"
    header_line2_re = r"^Current configuration.*$"
    header_line3_re = r"^!Running configuration.*$"

    # Strip the service timestamps comments
    service_timestamps1_re = r"^! Last configuration change at.*$"
    service_timestamps2_re = r"^! NVRAM config last updated at.*$"
    service_timestamps3_re = r"^! No configuration change since last restart.*$"

    # Strip misc
    misc1_re = r'^ntp clock-period.*$'
    misc2_re = r'^!Time.*$'

    for pattern in [header_line1_re, header_line2_re, header_line3_re,
                    service_timestamps1_re, service_timestamps2_re, 
                    service_timestamps3_re, misc1_re, misc2_re]:
        cfg = re.sub(pattern, "", cfg, flags=re.M).lstrip()
    return cfg


def configure_diff(device, configuration=None, **kwargs):

    if configuration:
        # get running config as dict

        config_pre = device['nc'].send_command('show run')
        config_pre = config_filter_cisco_ios(config_pre)
        config_pre = config_pre.split('\n')

        # deploy
        result = device['nc'].send_config_set(configuration)

        # get running config as dict
        config_post = device['nc'].send_command('show run')
        config_post = config_filter_cisco_ios(config_post)
        config_post = config_post.split('\n')

        #save?

        # diff
        output = '\n'.join(difflib.context_diff(config_pre, config_post))

    else:
        output = 'You need a configuration to deploy for this example.'

    return output