from boltons.remerge import remerge


hosts = {
        'r1': {
            'netmiko-ssh': {
                'host': 'r1'
            },
            'scrapli-asyncssh': {
                'host': 'r1'
            },
            'scrapli-ssh': {
                'host': 'r1'
            },
            'groups': ['group1','group3'],
            'roles': ['roleA'],
        },
        'r2': {
           'netmiko-ssh': {
                'host': 'r2',
                'password': 'dummy'
            }, 
            'scrapli-asyncssh': {
                'host': 'r2'
            },
            'scrapli-ssh': {
                'host': 'r2'
            },
            'groups': ['group3','group1'],
            'roles': ['roleB'],
        },
        'r3': {
            'netmiko-ssh': {
                'host': 'r3'
            },
            'scrapli-asyncssh': {
                'host': 'r3'
            },
            'scrapli-ssh': {
                'host': 'r3'
            },
            'groups': ['group1','group3'],
            'roles': ['roleA'],
        },
        'r4': {
           'netmiko-ssh': {
                'host': 'r4'
            }, 
            'scrapli-asyncssh': {
                'host': 'r4'
            },
            'scrapli-ssh': {
                'host': 'r4'
            },
            'groups': ['group3','group1'],
            'roles': ['roleB'],
        },
        'r5': {
           'netmiko-ssh': {
                'host': 'r5'
            }, 
            'scrapli-asyncssh': {
                'host': 'r5'
            },
            'scrapli-ssh': {
                'host': 'r5'
            },
        },
        'r6': {
           'netmiko-ssh': {
                'host': 'r6'
            }, 
            'scrapli-asyncssh': {
                'host': 'r6'
            },
            'scrapli-ssh': {
                'host': 'r6'
            },
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
    'netmiko-ssh': {
        'device_type': 'cisco_ios',
        'username': 'fred',
        'password': 'bedrock',
        'secret': '',
        'port': 22,
        'fast_cli': False
    },
    'scrapli-asyncssh': {
        "auth_username": 'fred',
        "auth_password": 'bedrock',
        "platform": "cisco_iosxe",
        "transport": "asyncssh",
        "auth_strict_key": False,
        "ssh_config_file": '/workspace/vagrant/.ssh/config'
    },
    'scrapli-ssh': {
        "auth_username": 'fred',
        "auth_password": 'bedrock',
        "platform": "cisco_iosxe",
        "transport": "ssh2",
        "auth_strict_key": False,
        "ssh_config_file": '/workspace/vagrant/.ssh/config'
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