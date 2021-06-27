from netmiko import ConnectHandler
#from netmiko import NetmikoTimeoutException, NetmikoAuthenticationException

#task_wrapper also comes in handy for handling subtasks
from runners import task_wrapper


# The primary task
def nm_task(device, **kwargs):

    # pop out any additional kwargs you may have passed
    #example = kwargs.pop('example', [])

    tasks = kwargs.pop('tasks', [])

    # will return a dictionary
    output = {}

    # connect to device
    remote_conn = ConnectHandler(**device['conn'])

    device['netmiko'] = remote_conn

    for task in tasks:
        # inject ret as run_dict in case you wanted to use the output from previous subtasks.
        # kind of like ansible register but automatic and accessible in subtasks functions with
        # run_dict = kwargs.pop('run_dict', {})
        # basic_command = run_dict.get('basic_command', {})
        # where basic_command is also a dict with result as a key
        task['kwargs']['run_dict'] = output

        # run subtask
        output[task['name']] = task_wrapper(task=task['function'], device=device, **task['kwargs'])

        # subtasks may return an 'exception', as we are using task_wrapper,
        # or you could add a 'failed' key in the return output of a subtask
        # you could choose to break out of this task loop here
        # instead of continuing through the remaining subtasks

    #disconnect from device
    device['netmiko'].disconnect()

    return output