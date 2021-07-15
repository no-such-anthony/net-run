def custom2(device, **kwargs):

    tasks = kwargs.pop('tasks', [])

    for task in tasks:
        print('device = ', device['name'])
        task['function']()

    # return either a dictionary with at least a 'result' key/value pair, or simply a string/integer
    output = {}
    output['result'] = "it's evolving!"
    return output

# need at least a primary_task pointing to a callable function
taskbook = {}
taskbook['primary_task'] = 'taskbooks.custom2.custom2'

# add some tasks
taskbook['kwargs'] = {}

tasks = [
        {
            'name': 'print_hello',
            'function': 'subtasks.custom.print_hello.print_hello',
            'kwargs': { }
        },
        {
            'name': 'print_hello',
            'function': 'subtasks.custom.print_hello.print_hello',
            'kwargs': { }
        },
        ]

taskbook['kwargs']['tasks'] = tasks
