#!/usr/bin/env python

# no-such-anthony
# https://github.com/no-such-anthony/net-run


import argparse
import sys
from datetime import datetime

from inventory.inventory import get_inventory
from utils.utils import cl_filter
from utils.utils import import_taskbook
from utils.utils import print_output

from runners.runners import WithThreadPool
from runners.runners_async import withSemaphore


def main(args):

    # load inventory
    inventory = get_inventory()
    #pprint(inventory)
    #sys.exit()
    
    # command line filtering
    inventory = cl_filter(inventory, args)

    # tasks import
    taskbook = import_taskbook(args.taskbook)

    # start timer
    start_time = datetime.now()

    if taskbook['async']:
        # Load task runner
        runner = withSemaphore(10)

    else:
        # Load task runner
        runner = WithThreadPool(10)

    # You can also send additional arguments which will be passed to the task        
    output = runner.run(taskbook['primary_task'], name="Run example tasks", inventory=inventory, **taskbook.get('kwargs',{}))

    #stop timer
    elapsed_time = datetime.now() - start_time

    # Print task results 
    print_output(output)

    print('-'*50)
    print("Elapsed time: {}".format(elapsed_time))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--device', type=str, nargs='+', required=False)
    parser.add_argument('--group', type=str, nargs='+', required=False)
    parser.add_argument('--role', type=str, nargs='+', required=False)
    parser.add_argument('--taskbook', type=str, required=True)
    args = parser.parse_args()

    main(args)
