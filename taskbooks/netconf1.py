taskbook = {}


taskbook['primary_task'] = 'tasks.task_default.task_default'

taskbook['kwargs'] = {}
taskbook['kwargs']['connection_type'] = 'ncclient'
taskbook['kwargs']['connection_key'] = 'ncclient'

tasks = [
        {
            'name': 'get_config',
            'function': 'subtasks.ncclient.get_config_command',
            'kwargs': { 'source' : 'running'}
        },
        ]

tasks = [tasks[0]]
taskbook['kwargs']['tasks'] = tasks




