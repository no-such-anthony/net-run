tasks = [
        {
            'name': 'Get config',
            'function': 'ncclient_get_config.ncclient_get_config',
            'kwargs': { 'source' : 'running'}
        },
        ]

tasks = [tasks[0]]

taskbook = {}
taskbook['append_paths'] = ['subtasks/with_ncclient/','tasks/']
taskbook['primary_task'] = 'task_default.task_default'

taskbook['kwargs'] = {}
taskbook['name'] = "Testing with ncclient!"
taskbook['kwargs']['connection_type'] = 'ncclient'
taskbook['kwargs']['connection_key'] = 'ncclient'

taskbook['kwargs']['tasks'] = tasks