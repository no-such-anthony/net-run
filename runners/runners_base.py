from concurrent.futures import ThreadPoolExecutor, as_completed
import traceback

    
def task_wrapper(**kwargs):

    task = kwargs.pop('task', None)
    device = kwargs.pop('device', None)
    task_name = kwargs.pop('name', None)
    result = {}
    result['device'] = device['name']
    result['task'] = task_name or task.__name__

    try:
        result['result'] = task(device, **kwargs)

    except Exception as e:
        result['exception'] = e
        result['result'] = traceback.format_exc()

    return result


class WithThreadPool(object):

    # as_completed is great if you want a progress bar or stop on an exception/failure?

    def __init__(self, num_workers: int = 20) -> None:
        self.num_workers = num_workers

    def run(self, task, name = None, inventory = None, **kwargs):

        # inject positional argument 'task' into kwargs for use in task
        kwargs['task'] = task
        results = {}
        results['task'] = name or task.__name__
        results['devices'] = []

        with ThreadPoolExecutor(max_workers=self.num_workers) as pool:
            futures = {pool.submit(task_wrapper, device=device, **kwargs): device for device in inventory.values()}
            for future in as_completed(futures):
                worker_result = future.result()
                results['devices'].append(worker_result)

        return results


class WithLoop(object):

    def __init__(self, num_workers: int = 20) -> None:
        # num_workers doesn't actually do anything in serial/loop mode.
        pass

    def run(self, task, name = None, inventory = None, **kwargs):

        # inject positional argument 'task' into kwargs for use in task
        kwargs['task'] = task
        results = {}
        results['task'] = name or task.__name__
        results['devices'] = []

        for device in inventory.values():
            worker_result = task_wrapper(device=device, **kwargs)
            results['devices'].append(worker_result)

        return results