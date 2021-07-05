from netmiko import ConnectHandler
#from netmiko import NetmikoTimeoutException, NetmikoAuthenticationException

#task_wrapper also comes in handy for handling subtasks if you decide to use them
from runners import task_wrapper


# The primary task
def task_netmiko(device, **kwargs):

    # pop out any additional kwargs you may have passed
    #example = kwargs.pop('example', [])

    tasks = kwargs.pop('tasks', [])

    # will return a dictionary
    output = []

    # connect to device
    remote_conn = ConnectHandler(**device['netmiko-ssh'])

    device['nc'] = remote_conn

    for task in tasks:
        # inject output as run_output into kwargs case you need the output from previous subtasks.
        # eg run_output = kwargs.pop('run_output', [])
        task['kwargs']['run_output'] = output

        # run subtask
        output.append(task_wrapper(task=task['function'], device=device, **task['kwargs']))

        # subtasks may return an 'exception', as we are using task_wrapper,
        # or you could add a 'failed' key in the return output of a subtask
        # you could choose to break out of this task loop here
        # instead of continuing through the remaining subtasks

    remote_conn.disconnect()

    # if required  you want you can change output to a dict with at least a 'result' key, or str/int,
    # or append another dict with at least 'result' and 'task' keys.
    # eg output.append({'task':'Final','result': 'Complete.'})

    return output