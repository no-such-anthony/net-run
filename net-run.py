#!/usr/bin/env python

# no-such-anthony
# https://github.com/no-such-anthony/net-run


import argparse
import sys
import importlib
from pprint import pprint

from inventory import get_inventory
from runners import WithThreadPool
from nm_task import nm_task


# Using netmiko 4 devel
# pip install git+https://github.com/ktbyers/netmiko.git@develop

#import logging
#logging.basicConfig(filename='test.log', level=logging.DEBUG)
#logger = logging.getLogger("netmiko")

def main(args):

    # load inventory
    inventory = get_inventory()
    #pprint(inventory)
    #sys.exit()
    
    # filter devices with any command-line arguments used
    if args.device:
        inventory = { k:v for (k,v) in inventory.items() if k in args.device }

    if args.group:
        inventory = { k:v for (k,v) in inventory.items() if any(x in v['groups'] for x in args.group) }

    if args.role:
        inventory = { k:v for (k,v) in inventory.items() if any(x in v['roles'] for x in args.role) }

    # Load task runner
    runner = WithThreadPool(4)

    tasks = importlib.import_module(f"taskbooks.{args.taskbook}").tasks
    if not isinstance(tasks, list):
        print('Tasks should be a list.')
        sys.exit()

    # You can also send additional arguments which will be passed to the task        
    output = runner.run(nm_task, name="Run example tasks", inventory=inventory, tasks=tasks)

    # Print task results
    print(f"Task = {output['task']}")
    
    for device, task_output in sorted(output['devices'].items()):
        print('='*20,f"Results for {device}",'='*20)
        if 'exception' not in task_output:
            # if no exception in main loop we should have a dictionary
            for k,v in task_output['result'].items():
                print('-'*len(k))
                print(k)
                print('-'*len(k))
                print(v['result'])
                print()
        else:
            print(task_output['result'])
    print()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--device', type=str, nargs='+', required=False)
    parser.add_argument('--group', type=str, nargs='+', required=False)
    parser.add_argument('--role', type=str, nargs='+', required=False)
    parser.add_argument('--taskbook', type=str, required=True)
    args = parser.parse_args()

    main(args)
