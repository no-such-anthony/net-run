import traceback
import asyncio


# got the semaphore idea from https://asyncpyneng.readthedocs.io/ru/latest/book/using_asyncio/semaphore.html


class withSemaphore(object):
    def __init__(self, num_workers: int = 20) -> None:
        self.num_workers = num_workers

    async def run(self, task, name=None, inventory=None, **kwargs):

        # inject positional argument 'task' into kwargs for use in task
        kwargs['task'] = task
        results = {}
        results['task'] = name or task.__name__
        results['devices'] = []

        semaphore = asyncio.Semaphore(self.num_workers)

        coroutines = [
            task_wrapper_with_semaphore(semaphore, device=device, **kwargs)
            for device in inventory.values()
            ]
        result = await asyncio.gather(*coroutines)

        #fix the data so it matches schema that print_output is expecting
        results['devices'] = result

        return results


async def task_wrapper_with_semaphore(semaphore, **kwargs):

    task = kwargs.pop('task', None)
    device = kwargs.pop('device', None)

    result = {}
    result['device'] = device['name']

    async with semaphore:
        try:
            result['result'] = await task(device, **kwargs)
        except Exception as e:
            result['exception'] = e
            result['result'] = traceback.format_exc()

    return result


async def task_wrapper(**kwargs):

    task = kwargs.pop('task', None)
    device = kwargs.pop('device', None)
    result = {}
    result['device'] = device['name']

    try:
        result['result'] = await task(device, **kwargs)

    except Exception as e:
        result['exception'] = e
        result['result'] = traceback.format_exc()

    return result