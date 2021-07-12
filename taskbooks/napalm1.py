taskbook = {}


taskbook['primary_task'] = 'tasks.task_default.task_default'

taskbook['kwargs'] = {}
taskbook['kwargs']['connection_type'] = 'napalm'
taskbook['kwargs']['connection_key'] = 'napalm-ssh'

tasks = [
        {
            'name': 'basic_command',
            'function': 'subtasks.napalm.basic_command',
            'kwargs': { 'command' : ['show version | i uptime']}
        },
        ]

tasks = [tasks[0]]
taskbook['kwargs']['tasks'] = tasks

