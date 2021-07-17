import random

#import sys
#from pathlib import Path
#append_paths = ['subtasks/netmiko/','tasks/']
#for p in append_paths:
#    sys.path.append(str(Path(p).resolve()))

tasks = [
        {
            'name': 'basic_command',
            'function': 'basic_command.basic_command',
            'kwargs': { 'command' : 'show version | i uptime'}
        },
        {
            'name': 'copy_command',
            'function': 'copy_command.copy_command',
            'kwargs': { 
                    'source': 'running-config',
                    'destination': 'tftp://192.168.204.1',
                    'ckwargs' : { 'read_timeout': 100 }
                    }
        },
        {
            'name': 'parse_command',
            'function': 'basic_command.basic_command',
            'kwargs': { 'command' : 'show version',
                        'ckwargs': { 'use_textfsm': True}
                      }
        },
        {
            'name': 'send_config',
            'function': 'send_config.send_config',
            'kwargs': { 
                    'configuration' : ["service timestamps debug datetime msec",
                                        "service timestamps log datetime msec"] 
                    }
        },
        {
            'name': 'configure_diff',
            'function': 'configure_diff.configure_diff',
            'kwargs':  { 'configuration':  [f"interface lo100",
                                            f"description random={random.randrange(100, 1000, 3)}"]
                    }
        },
        {
            'name': 'ping_ips',
            'function': 'ping_ips.ping_ips',
            'kwargs':  { 'ips':  ['10.0.12.1','10.0.12.2','10.0.1.1'],
                         'command': 'ping {{ip}} repeat 5 timeout 1',
                         'ckwargs': { 'read_timeout': 10},
                         }
        },
        ]

tasks = [tasks[0]]

taskbook = {}
taskbook['append_paths'] = ['subtasks/netmiko/','tasks/']
taskbook['primary_task'] = 'task_default.task_default'

taskbook['kwargs'] = {}
taskbook['kwargs']['connection_type'] = 'netmiko'
taskbook['kwargs']['connection_key'] = 'netmiko-ssh'

taskbook['kwargs']['tasks'] = tasks

#todo: taskbook filter, subtask filter?
#todo: different subtask connection?