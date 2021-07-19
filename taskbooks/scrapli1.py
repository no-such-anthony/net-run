import random


tasks = [
        {
            'name': 'A simple command',
            'function': 'scrapli_command.scrapli_command',
            'kwargs': { 'command' : 'show version | i uptime'}
        },
        ]

tasks = [tasks[0]]

taskbook = {}
taskbook['append_paths'] = ['subtasks/with_scrapli/','tasks/']
taskbook['primary_task'] = 'task_default.task_default'

taskbook['kwargs'] = {}
taskbook['kwargs']['connection_type'] = 'scrapli'
taskbook['kwargs']['connection_key'] = 'scrapli-ssh'

taskbook['kwargs']['tasks'] = tasks