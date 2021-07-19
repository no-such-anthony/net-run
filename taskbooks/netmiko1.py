import random

#import sys
#from pathlib import Path
#append_paths = ['subtasks/netmiko/','tasks/']
#for p in append_paths:
#    sys.path.append(str(Path(p).resolve()))

tasks = [
        {
            'name': 'A simple command',
            'function': 'netmiko_command.netmiko_command',
            'kwargs': { 'command' : 'show version | i uptime'}
        },
        {
            'name': 'A general copy',
            'function': 'netmiko_copy.netmiko_copy',
            'kwargs': { 
                    'source': 'running-config',
                    'destination': 'tftp://192.168.204.1',
                    'ckwargs' : { 'read_timeout': 100 }
                    }
        },
        {
            'name': 'A parser example with textfsm',
            'function': 'netmiko_command.netmiko_command',
            'kwargs': { 'command' : 'show version',
                        'ckwargs': { 'use_textfsm': True}
                      }
        },
        {
            'name': 'Simple configuration task',
            'function': 'netmiko_config.netmiko_config',
            'kwargs': { 
                    'configuration' : ["service timestamps debug datetime msec",
                                        "service timestamps log datetime msec"] 
                    }
        },
        {
            'name': 'Various ways of diff',
            'function': 'netmiko_config_diffs.netmiko_config_diffs',
            'kwargs':  { 'configuration':  [f"interface lo100",
                                            f"description random={random.randrange(100, 1000, 3)}"]
                    }
        },
        {
            'name': 'Ping example',
            'function': 'netmiko_ping_ips.netmiko_ping_ips',
            'kwargs':  { 'ips':  ['10.0.12.1','10.0.12.2','10.0.1.1'],
                         'command': 'ping {{ip}} repeat 5 timeout 1',
                         'ckwargs': { 'read_timeout': 10},
                         }
        },
        ]

#tasks = [tasks[0]]

taskbook = {}
taskbook['append_paths'] = ['subtasks/with_netmiko/','tasks/']
taskbook['primary_task'] = 'task_default.task_default'

taskbook['kwargs'] = {}
taskbook['kwargs']['connection_type'] = 'netmiko'
taskbook['kwargs']['connection_key'] = 'netmiko-ssh'

taskbook['kwargs']['tasks'] = tasks

#todo: taskbook filter, subtask filter?
#todo: different subtask connection?