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
    output = {}

    # connect to device
    async with AsyncScrapli(**device['scrapli-asyncssh']) as remote_conn:

        device['nc'] = remote_conn

        for task in tasks:
            # inject ret as run_dict in case you wanted to use the output from previous subtasks.
            # kind of like ansible register but automatic and accessible in subtasks functions with
            # run_dict = kwargs.pop('run_dict', {})
            # basic_command = run_dict.get('basic_command', {})
            # where basic_command is also a dict with result as a key
            task['kwargs']['run_dict'] = output

            # run subtask
            output[task['name']] = await task_wrapper(task=task['function'], device=device, **task['kwargs'])

            # subtasks may return an 'exception', as we are using task_wrapper,
            # or you could add a 'failed' key in the return output of a subtask
            # you could choose to break out of this task loop here
            # instead of continuing through the remaining subtasks

    return output