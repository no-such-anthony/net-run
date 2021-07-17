tasks = [
        {
            'name': 'basic_command',
            'function': 'basic_command.basic_command',
            'kwargs': { 'command' : 'show version | i uptime'}
        },

        ]

tasks = [tasks[0]]

taskbook = {}
taskbook['async'] = True
taskbook['append_paths'] = ['subtasks/scrapli_async/','tasks/']
taskbook['primary_task'] = 'task_default_async.task_default'

taskbook['kwargs'] = {}
taskbook['kwargs']['connection_type'] = 'scrapli'
taskbook['kwargs']['connection_key'] = 'scrapli-asyncssh'

taskbook['kwargs']['tasks'] = tasks