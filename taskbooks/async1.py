tasks = [
        {
            'name': 'A simple command',
            'function': 'scrapli_command.scrapli_command',
            'kwargs': { 'command' : 'show version | i uptime'}
        },

        ]

tasks = [tasks[0]]

taskbook = {}
taskbook['name'] = "Testing with Scrapli Async!"
taskbook['async'] = True
taskbook['append_paths'] = ['subtasks/with_scrapli_async/','tasks/']
taskbook['primary_task'] = 'task_default_async.task_default'

taskbook['kwargs'] = {}
taskbook['kwargs']['connection_type'] = 'scrapli'
taskbook['kwargs']['connection_key'] = 'scrapli-asyncssh'

taskbook['kwargs']['tasks'] = tasks