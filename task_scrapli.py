import asyncio

from scrapli import AsyncScrapli
#from scrapli.exceptions import ScrapliException

#task_wrapper also comes in handy for handling subtasks
from runners_async import task_wrapper


# The primary task
async def task_scrapli(device, **kwargs):

    # pop out any additional kwargs you may have passed
    #example = kwargs.pop('example', [])

    tasks = kwargs.pop('tasks', [])

    # will return a dictionary
    output = []

    # connect to device
    remote_conn = AsyncScrapli(**device['scrapli-asyncssh'])
    await remote_conn.open()

    device['nc'] = remote_conn

    for task in tasks:
        # inject output as run_output into kwargs case you need the output from previous subtasks.
        # eg run_output = kwargs.pop('run_output', [])
        task['kwargs']['run_output'] = output

        # run subtask
        output.append(await task_wrapper(task=task['function'], device=device, **task['kwargs']))

        # subtasks may return an 'exception', as we are using task_wrapper,
        # or you could add a 'failed' key in the return output of a subtask
        # you could choose to break out of this task loop here
        # instead of continuing through the remaining subtasks

    await remote_conn.close()

    return output