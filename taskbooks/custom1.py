#from connections import get_connection, close_connection

def custom1(device, **kwargs):

    # pop out any additional kwargs you may have passed
    #tasks = kwargs.pop('tasks', [])
    #connection_type = kwargs.pop('connection_type', '')
    #connection_key = kwargs.pop('connection_key', '')

    # connect to device
    #device['nc'] = get_connection(device, connection_type, connection_key)

    print('device = ', device['name'])

    #close_connection(device['nc'], connection_type)

    # return either a dictionary with at least a 'result' key/value pair, or simply a string/integer
    output = {}
    output['result'] = "it's evolving!"
    return output

taskbook = {}

# need at least a primary_task pointing to a callable function
taskbook['name'] = "Custom, example 1!"
taskbook['primary_task'] = custom1

taskbook['kwargs'] = {}
#taskbook['kwargs']['connection_type'] = None
#taskbook['kwargs']['connection_key'] = None
#taskbook['kwargs']['tasks'] = []
