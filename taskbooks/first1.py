import nm_subtasks
import random

# A task list helps with experimentating.
# With the side effect that it kind of looks like an ansible playbook...
tasks = [
        {
            'name': 'basic_command',
            'function': nm_subtasks.basic_command,
            'kwargs': { 'command' : 'show version | inc uptime'}
        },
        {
            'name': 'multiline_command',
            'function': nm_subtasks.multiline_command,
            'kwargs': { 
                    'command' : [['copy running-config tftp://192.168.204.1','Address or name of remote host'],
                                 ['', 'Destination filename'],
                                 ['', '#']],
                    'ckwargs' : { 'read_timeout': 100 }
                    }
        },
        {
            'name': 'parse_command',
            'function': nm_subtasks.basic_command,
            'kwargs': { 'command' : 'show version',
                        'ckwargs': { 'use_textfsm': True}
                      }
        },
        {
            'name': 'send_config',
            'function': nm_subtasks.send_config,
            'kwargs': { 
                    'configuration' : ["service timestamps debug datetime msec",
                                        "service timestamps log datetime msec"] 
                    }
        },
        {
            'name': 'configure_diff',
            'function': nm_subtasks.configure_diff,
            'kwargs':  { 'configuration':  [f"interface lo100",
                                            f"description random={random.randrange(100, 1000, 3)}"]
                    }
        },
        {
            'name': 'ping_ips',
            'function': nm_subtasks.ping_ips,
            'kwargs':  { 'ips':  ['10.0.12.1','10.0.12.2','10.0.1.1'],
                         'multi_ping':  [ 
                            ["ping", r"ip"],
                            ["", r"Target IP address"],
                            ["{{ip}}", "Repeat count"],
                            ["5", "Datagram size"],
                            ["", "Timeout in seconds"],
                            ["", "Extended"],
                            ["", "Sweep"],
                            ["", ""],],
                         'ckwargs': { 'read_timeout': 100 },
                                        }
        },
        ]

#tasks = [tasks[0],tasks[5]]