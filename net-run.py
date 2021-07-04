#!/usr/bin/env python

# no-such-anthony
# https://github.com/no-such-anthony/net-run


import argparse
import sys
from datetime import datetime

from inventory import get_inventory
from utils import cl_filter
from utils import import_taskbook
from utils import print_output

from runners import WithThreadPool
from runners_async import withSemaphore


# Using netmiko 4 devel and async scrapli
#
# pip install git+https://github.com/ktbyers/netmiko.git@develop
#
# pip install scrapli
# pip install asyncssh
# pip install scrapli_community


def main(args):

    # load inventory
    inventory = get_inventory()
    #pprint(inventory)
    #sys.exit()
    
    # command line filtering
    inventory = cl_filter(inventory, args)

    # tasks import
    taskbook = import_taskbook(args.taskbook)
    master_task = taskbook.pop('master_task', None)
    use_async = taskbook.pop('async', False)

    # start timer
    start_time = datetime.now()

    if use_async:
        # Load task runner
        runner = withSemaphore(10)

    else:
        # Load task runner
        runner = WithThreadPool(10)

    # You can also send additional arguments which will be passed to the task        
    output = runner.run(master_task, name="Run example tasks", inventory=inventory, taskbook=taskbook)

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
