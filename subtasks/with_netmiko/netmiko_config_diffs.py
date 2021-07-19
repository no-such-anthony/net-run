import re

# Using python stnandard library
import difflib
# Using netuils library
from netutils.config import compliance
# Using PyATS/Genie library
from genie.libs.sdk.apis.utils import compare_config_dicts, get_config_dict


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


def netmiko_config_diffs(device, configuration=None, **kwargs):

    if configuration:
        # get running config as dict

        config_pre = device['nc'].send_command('show run')
        config_pre = config_filter_cisco_ios(config_pre)

        # deploy
        result = device['nc'].send_config_set(configuration)

        # get running config as dict
        config_post = device['nc'].send_command('show run')
        config_post = config_filter_cisco_ios(config_post)

        #save?

        # diff
        output = {}

        output['difflib'] = '\n'.join(difflib.context_diff(config_pre.split('\n'), config_post.split('\n')))

        # diff with netutils
        output['netutils'] = compliance._check_configs_differences(config_pre, config_post, 'cisco_ios')

        # diff with PyATS/Genie
        # in this case you probably also skip "config_filter_cisco_ios" as similar functionality should be builtin
        # as diff is built from a dict diff you may want to tidy up and remove the trailing : from each line
        diff = compare_config_dicts(get_config_dict(config_pre), get_config_dict(config_post))
        output['genie'] = re.sub(r":$", "", str(diff), flags=re.M)


    else:
        output = 'You need a configuration to deploy for this example.'

    return output