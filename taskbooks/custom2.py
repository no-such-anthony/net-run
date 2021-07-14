#from connections import get_connection, close_connection

def custom2(device, **kwargs):

    # pop out any additional kwargs you may have passed
    tasks = kwargs.pop('tasks', [])
    #connection_type = kwargs.pop('connection_type', '')
    #connection_key = kwargs.pop('connection_key', '')

    # connect to device
    #device['nc'] = get_connection(device, connection_type, connection_key)

    for task in tasks:
        print('device = ', device['name'])
        task['function']()
        #task_wrapper(task=task['function'], device=device, **task['kwargs'])

    #close_connection(device['nc'], connection_type)

    # return either a dictionary with at least a 'result' key/value pair, or simply a string/integer
    output = {}
    output['result'] = "it's evolving!"
    return output

taskbook = {}

# need at least a primary_task pointing to a callable function
taskbook['primary_task'] = 'taskbooks.custom2.custom2'

taskbook['kwargs'] = {}
#taskbook['kwargs']['connection_type'] = None
#taskbook['kwargs']['connection_key'] = None

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
