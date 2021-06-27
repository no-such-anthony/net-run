from boltons.remerge import remerge


hosts = {
        'r1': {
            'conn': {
                'host': 'r1'
            },
            'groups': ['group1','group3'],
            'roles': ['roleA'],
        },
        'r2': {
           'conn': {
                'host': 'r2'
            }, 
            'groups': ['group3','group1'],
            'roles': ['roleB'],
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
    'conn': {
        'device_type': 'cisco_ios',
        'username': 'fred',
        'password': 'bedrock',
        'secret': '',
        'port': 22,
        'fast_cli': False
    },
}


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