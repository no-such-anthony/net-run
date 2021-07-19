tasks = [
        {
            'name': 'A simple command',
            'function': 'napalm_command.napalm_command',
            'kwargs': { 'command' : ['show version | i uptime']}
        },
        ]

tasks = [tasks[0]]

taskbook = {}
taskbook['append_paths'] = ['subtasks/with_napalm/','tasks/']
taskbook['primary_task'] = 'task_default.task_default'

taskbook['kwargs'] = {}
taskbook['kwargs']['connection_type'] = 'napalm'
taskbook['kwargs']['connection_key'] = 'napalm-ssh'

taskbook['kwargs']['tasks'] = tasks