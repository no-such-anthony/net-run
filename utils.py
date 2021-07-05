import importlib
import sys
from pprint import pprint

def cl_filter(inventory, args):
    # filter devices with any command-line arguments used
    if args.device:
        inventory = { k:v for (k,v) in inventory.items() if k in args.device }

    if args.group:
        inventory = { k:v for (k,v) in inventory.items() if any(x in v['groups'] for x in args.group) }

    if args.role:
        inventory = { k:v for (k,v) in inventory.items() if any(x in v['roles'] for x in args.role) }

    return inventory


def import_taskbook(taskbook):
    taskbook_dict = importlib.import_module(f"taskbooks.{taskbook}").taskbook
    if not isinstance(taskbook_dict, dict):
        print('Taskbook should be a dictionary.')
        sys.exit()
    return taskbook_dict


def import_primary_task(primary_task):
    p, m = primary_task.rsplit('.', 1)
    mod = importlib.import_module(p)
    return getattr(mod, m)


def import_if_req(tasks):
    for task in tasks:
        if isinstance(task['function'], str):
            p, m = task['function'].rsplit('.', 1)
            mod = importlib.import_module(p)
            task['function'] = getattr(mod, m)
        if not callable(task['function']):
            print('Subtasks in the task list should be callables.')
            sys.exit()
    return tasks


def print_output(output):

    # Print task results
    print(f"Task = {output['task']}")

    for result in sorted(output['devices'], key=lambda k: k['device']):
        print('='*20,f"Results for {result['device']}",'='*20)
        if 'exception' not in result:
            # if no exception in main loop we should have a dictionary or a list of dictionaries
            # each containing a 'result'
            if isinstance(result['result'], list):
                for r in result['result']:
                    print('-'*len(r['task']))
                    print(r['task'])
                    print('-'*len(r['task']))
                    print(r['result'])
                    print()
            elif isinstance(result['result'], dict):
                print(result['result']['result']) # definitely needs improvement!
            else:
                print(result['result'])    
        else:
            print(result['result'])
    print()

