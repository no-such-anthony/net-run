print('importing...')

tasks = [
        {
            'name': 'print_hello',
            'function': 'print_hello.print_hello',
            'kwargs': { }
        },
        {
            'name': 'print_hello',
            'function': 'custom2.print_hello2',
            'kwargs': { }
        },
        ]


def print_hello2():
    print('this hello')


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
taskbook['primary_task'] = 'custom2.custom2'
taskbook['append_paths'] = ['subtasks/custom/']

# add some tasks
taskbook['kwargs'] = {}
taskbook['kwargs']['tasks'] = tasks