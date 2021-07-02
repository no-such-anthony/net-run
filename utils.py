import importlib
import sys

def cl_filter(inventory, args):
    # filter devices with any command-line arguments used
    if args.device:
        inventory = { k:v for (k,v) in inventory.items() if k in args.device }

    if args.group:
        inventory = { k:v for (k,v) in inventory.items() if any(x in v['groups'] for x in args.group) }

    if args.role:
        inventory = { k:v for (k,v) in inventory.items() if any(x in v['roles'] for x in args.role) }

    return inventory


def tasks_import(taskbook):
    tasks = importlib.import_module(f"taskbooks.{taskbook}").tasks
    if not isinstance(tasks, list):
        print('Tasks should be a list.')
        sys.exit()
    return tasks


def print_output(output):

    # Print task results
    print(f"Task = {output['task']}")

    for result in sorted(output['devices'], key=lambda k: k['device']):
        print('='*20,f"Results for {result['device']}",'='*20)
        if 'exception' not in result:
            # if no exception in main loop we should have a dictionary
            for k,v in result['result'].items():
                print('-'*len(k))
                print(k)
                print('-'*len(k))
                print(v['result'])
                print()
        else:
            print(result['result'])
    print()

