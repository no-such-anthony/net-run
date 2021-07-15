
taskbook = {}
taskbook['async'] = True
taskbook['primary_task'] = 'tasks.task_default_async.task_default'

taskbook['kwargs'] = {}
taskbook['kwargs']['connection_type'] = 'scrapli'
taskbook['kwargs']['connection_key'] = 'scrapli-asyncssh'

tasks = [
        {
            'name': 'basic_command',
            'function': 'subtasks.scrapli_async.basic_command.basic_command',
            'kwargs': { 'command' : 'show version | i uptime'}
        },

        ]

#tasks = [tasks[0],tasks[5]]

taskbook['kwargs']['tasks'] = tasks
