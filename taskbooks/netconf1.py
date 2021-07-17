tasks = [
        {
            'name': 'get_config',
            'function': 'get_config_command.get_config_command',
            'kwargs': { 'source' : 'running'}
        },
        ]

tasks = [tasks[0]]

taskbook = {}
taskbook['append_paths'] = ['subtasks/ncclient/','tasks/']
taskbook['primary_task'] = 'task_default.task_default'

taskbook['kwargs'] = {}
taskbook['kwargs']['connection_type'] = 'ncclient'
taskbook['kwargs']['connection_key'] = 'ncclient'

taskbook['kwargs']['tasks'] = tasks