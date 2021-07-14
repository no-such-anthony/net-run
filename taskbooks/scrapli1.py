import random

taskbook = {}
taskbook['primary_task'] = 'tasks.task_default.task_default'

taskbook['kwargs'] = {}
taskbook['kwargs']['connection_type'] = 'scrapli'
taskbook['kwargs']['connection_key'] = 'scrapli-ssh'

tasks = [
        {
            'name': 'basic_command',
            'function': 'subtasks.scrapli.basic_command.basic_command',
            'kwargs': { 'command' : 'show version | i uptime'}
        },
        ]
tasks = [tasks[0]]

taskbook['kwargs']['tasks'] = tasks
