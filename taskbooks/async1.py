import subtasks_scrapli
import random

# A task list helps with experimentating.
# With the side effect that it kind of looks like an ansible playbook...
tasks = [
        {
            'name': 'basic_command',
            'function': subtasks_scrapli.basic_command,
            'kwargs': { 'command' : 'show version | inc uptime'}
        },

        ]

#tasks = [tasks[0],tasks[5]]