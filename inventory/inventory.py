from boltons.remerge import remerge


hosts = {
        'r1': {
            'groups': ['group1','group3'],
            'roles': ['roleA'],
        },
        'r2': {
            'host': 'r2',
            'netmiko-ssh': {
                'password': 'dummy'
            }, 
            'groups': ['group3','group1'],
            'roles': ['roleB'],
        },
        'r3': {
            'groups': ['group1','group3'],
            'roles': ['roleA'],
        },
        'r4': { 
            'groups': ['group3','group1'],
            'roles': ['roleB'],
        },
        'r5': {
            'host': 'r5'
        },
        'r6': {
        },
        'core1': {
            'platform': 'iosxr',
            'ncclient': {
                'host': 'sbx-iosxr-mgmt.cisco.com',
                'port': 22,
                'username': 'admin',
                'password': 'C1sco12345',
                'hostkey_verify': False,
                'device_params' :{'name':'iosxr'},
            },
        },
        'core2': {
            'restconf': {
                'host': 'sandbox-iosxe-latest-1.cisco.com',
                'username': 'developer',
                'password': 'C1sco12345',
            }
        }
        }


groups = {
        'group1': {
            'roles': ['role1']
        },
        'group3': {
            'roles': ['role3','roleC'],
            'groups': ['group4']
        },
        'group4': {
            'roles': ['role4']

        }
    }
    
defaults = {
    'username': 'fred',
    'password': 'bedrock',

    'netmiko-ssh': {
        'device_type': 'cisco_ios',
        'secret': '',
        'port': 22,
        'fast_cli': False
    },
    'scrapli-asyncssh': {
        "platform": "cisco_iosxe",
        "transport": "asyncssh",
        "auth_strict_key": False,
        "ssh_config_file": '/workspace/vagrant/.ssh/config'
    },
    'scrapli-ssh': {
        "platform": "cisco_iosxe",
        "transport": "ssh2",
        "auth_strict_key": False,
        "ssh_config_file": '/workspace/vagrant/.ssh/config'
    },
    'napalm-ssh': {
        "driver": 'ios',
        "optional_args": {}
    },
    'alt_creds': {
        'username': 'fred',
        'password': 'bedrock',
        'secret': ''
    }
}
#had to set an ssh config file for scrapli as asyncssh couldn't negotiate encryption with the old GNS3 Dynamips image in my lab


def group_chain(h_groups, g_groups):
    
    chain = []

    for g in h_groups:
        if g not in chain:
            chain.append(g)

        for sg in group_chain(g_groups[g].get('groups',[]), g_groups):
            if sg not in chain:
                chain.append(sg)

    return chain


def get_inventory():

    inventory = {}

    # read in hosts, groups, defaults dictionary however you see fit.
    # run any decryptions or get_pass for credentials if needed.

    # build an inventory dictionary with inheritance
    for k,v in hosts.items():
        
        v['name'] = k
        host_groups = group_chain(v.get('groups',[]), groups)

        gg = []
        for g in host_groups[::-1]:
            gg.append((g,groups[g]))

        merged = remerge([('defaults', defaults), *gg, (k, v)])
        inventory[k] = merged[1]
        inventory[k]['groups'] = host_groups

    return inventory