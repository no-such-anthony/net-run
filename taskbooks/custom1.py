taskbook = {}

def custom1(device, **kwargs):

    print('device = ', device['name'])

    # return either a dictionary with at least a 'result' key/value pair, or simply a string/integer
    output = {}
    output['result'] = "it's evolving!"
    return output

# need at least a primary_task pointing to a callable function
taskbook['primary_task'] = custom1
