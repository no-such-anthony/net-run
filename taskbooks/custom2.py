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
    print('another hello, this time from inside the taskbook.')


def custom2(device, **kwargs):

    tasks = kwargs.pop('tasks', [])

    print('device = ', device['name'])
    for task in tasks:
        task['function']()

    # return either a dictionary with at least a 'result' key/value pair, or simply a string/integer
    output = {}
    output['result'] = "it's evolving!"
    return output

# need at least a primary_task pointing to a callable function
taskbook = {}
taskbook['name'] = "Custom, example 1!"
taskbook['primary_task'] = 'custom2.custom2'
taskbook['append_paths'] = ['subtasks/custom','postjobs']
taskbook['run_mode'] = 'serial'
taskbook['post_jobs'] = ['postjobs.print_elapsed']

# add some tasks
taskbook['kwargs'] = {}
taskbook['kwargs']['tasks'] = tasks