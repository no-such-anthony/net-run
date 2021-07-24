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
taskbook['run_mode'] = 'async'
taskbook['num_workers'] = 5
taskbook['append_paths'] = ['subtasks/with_scrapli_async/','tasks/']
taskbook['primary_task'] = 'task_default_async.task_default'

taskbook['kwargs'] = {}
taskbook['kwargs']['connection_type'] = 'scrapli'
taskbook['kwargs']['connection_key'] = 'scrapli-asyncssh'

taskbook['kwargs']['tasks'] = tasks