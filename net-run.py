#!/usr/bin/env python

# no-such-anthony
# https://github.com/no-such-anthony/net-run


import argparse
import sys
from datetime import datetime

from inventory import get_inventory
from utils import cl_filter
from utils import tasks_import
from utils import print_output

from runners import WithThreadPool
from task_netmiko import task_netmiko

import asyncio
from runners_async import withSemaphore
from task_scrapli import task_scrapli


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
    tasks = tasks_import(args.taskbook)

    # start timer
    start_time = datetime.now()

    # Load task runner
    runner = WithThreadPool(4)

    # You can also send additional arguments which will be passed to the task        
    output = runner.run(task_netmiko, name="Run example tasks", inventory=inventory, tasks=tasks)

    #stop timer
    elapsed_time = datetime.now() - start_time

    # Print task results 
    print_output(output)

    print('-'*50)
    print("Elapsed time: {}".format(elapsed_time))



async def async_main(args):

    # load inventory
    inventory = get_inventory()
    #pprint(inventory)
    #sys.exit()

    # command line filtering
    inventory = cl_filter(inventory, args)

    # tasks import
    tasks = tasks_import(args.taskbook)

    # start timer
    start_time = datetime.now()

    # Load task runner
    runner = withSemaphore(4)

    # You can also send additional arguments which will be passed to the task 
    output = await runner.run(task_scrapli, name="Run example tasks", inventory=inventory, tasks=tasks)

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
    parser.add_argument('--async', dest='do_async', action='store_true')
    args = parser.parse_args()

    if args.do_async:
        asyncio.run(async_main(args))
    else:
        main(args)
