import random


tasks = [
        {
            'name': 'basic_command',
            'function': 'basic_command.basic_command',
            'kwargs': { 'command' : 'show version | i uptime'}
        },
        ]

tasks = [tasks[0]]

taskbook = {}
taskbook['append_paths'] = ['subtasks/scrapli/','tasks/']
taskbook['primary_task'] = 'task_default.task_default'

taskbook['kwargs'] = {}
taskbook['kwargs']['connection_type'] = 'scrapli'
taskbook['kwargs']['connection_key'] = 'scrapli-ssh'

taskbook['kwargs']['tasks'] = tasks