import random

taskbook = {}
taskbook['primary_task'] = 'tasks.task_default.task_default'
#taskbook['primary_task'] = task_default.task_default  # or this, with the relevant import above

taskbook['kwargs'] = {}
taskbook['kwargs']['connection_type'] = 'netmiko'
taskbook['kwargs']['connection_key'] = 'netmiko-ssh'


tasks = [
        {
            'name': 'basic_command',
            'function': 'subtasks.netmiko.basic_command.basic_command',
            # or 'function': subtasks.netmiko.basic_command, - with the relevant import above
            'kwargs': { 'command' : 'show version | i uptime'}
        },
        {
            'name': 'copy_command',
            'function': 'subtasks.netmiko.copy_command.copy_command',
            'kwargs': { 
                    'source': 'running-config',
                    'destination': 'tftp://192.168.204.1',
                    'ckwargs' : { 'read_timeout': 100 }
                    }
        },
        {
            'name': 'parse_command',
            'function': 'subtasks.netmiko.basic_command.basic_command',
            'kwargs': { 'command' : 'show version',
                        'ckwargs': { 'use_textfsm': True}
                      }
        },
        {
            'name': 'send_config',
            'function': 'subtasks.netmiko.send_config.send_config',
            'kwargs': { 
                    'configuration' : ["service timestamps debug datetime msec",
                                        "service timestamps log datetime msec"] 
                    }
        },
        {
            'name': 'configure_diff',
            'function': 'subtasks.netmiko.configure_diff.configure_diff',
            'kwargs':  { 'configuration':  [f"interface lo100",
                                            f"description random={random.randrange(100, 1000, 3)}"]
                    }
        },
        {
            'name': 'ping_ips',
            'function': 'subtasks.netmiko.ping_ips.ping_ips',
            'kwargs':  { 'ips':  ['10.0.12.1','10.0.12.2','10.0.1.1'],
                         'command': 'ping {{ip}} repeat 5 timeout 1',
                         'ckwargs': { 'read_timeout': 10},
                         }
        },
        ]

tasks = [tasks[0]]

taskbook['kwargs']['tasks'] = tasks

#todo: taskbook filter, subtask filter?
#todo: different subtask connection?