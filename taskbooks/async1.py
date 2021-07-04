from task_scrapli import task_scrapli
import subtasks_scrapli
import random

taskbook = {}
taskbook['async'] = True
taskbook['primary_task'] = task_scrapli

tasks = [
        {
            'name': 'basic_command',
            'function': subtasks_scrapli.basic_command,
            'kwargs': { 'command' : 'show version | i uptime'}
        },

        ]

#tasks = [tasks[0],tasks[5]]

taskbook['kwargs'] = {}
taskbook['kwargs']['tasks'] = tasks
