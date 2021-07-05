import random

taskbook = {}
taskbook['primary_task'] = 'task_netmiko.task_netmiko'
#taskbook['primary_task'] = task_netmiko.task_netmiko  # or this, with the import above

tasks = [
        {
            'name': 'basic_command',
            'function': 'subtasks_netmiko.basic_command',
            # or 'function': 'subtasks_netmiko.basic_command', - with the import above
            'kwargs': { 'command' : 'show version | i uptime'}
        },
        {
            'name': 'multiline_command',
            'function': 'subtasks_netmiko.multiline_command',
            'kwargs': { 
                    'command' : [['copy running-config tftp://192.168.204.1','Address or name of remote host'],
                                 ['', 'Destination filename'],
                                 ['', '#']],
                    'ckwargs' : { 'read_timeout': 100 }
                    }
        },
        {
            'name': 'parse_command',
            'function': 'subtasks_netmiko.basic_command',
            'kwargs': { 'command' : 'show version',
                        'ckwargs': { 'use_textfsm': True}
                      }
        },
        {
            'name': 'send_config',
            'function': 'subtasks_netmiko.send_config',
            'kwargs': { 
                    'configuration' : ["service timestamps debug datetime msec",
                                        "service timestamps log datetime msec"] 
                    }
        },
        {
            'name': 'configure_diff',
            'function': 'subtasks_netmiko.configure_diff',
            'kwargs':  { 'configuration':  [f"interface lo100",
                                            f"description random={random.randrange(100, 1000, 3)}"]
                    }
        },
        {
            'name': 'ping_ips',
            'function': 'subtasks_netmiko.ping_ips',
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

tasks = [tasks[0],tasks[3]]

taskbook['kwargs'] = {}
taskbook['kwargs']['tasks'] = tasks