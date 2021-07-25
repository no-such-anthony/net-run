#!/usr/bin/env python

# no-such-anthony
# https://github.com/no-such-anthony/net-run


import argparse
import sys
from datetime import datetime

from inventory.inventory import get_inventory
from utils.utils import cl_filter
from utils.utils import import_taskbook


def main(args):

    # tasks import
    taskbook = import_taskbook(args.taskbook)

    # load inventory
    taskbook['inventory'] = get_inventory()
    #pprint(taskbook['inventory'])
    #sys.exit()
    
    # command line filtering
    taskbook['inventory'] = cl_filter(taskbook['inventory'], args)
    #pprint(taskbook['inventory'])
    #sys.exit()

    # start timer
    start_time = datetime.now()

    # You can also send additional arguments which will be passed to the task   
    taskbook['output'] = taskbook['runner'].run(taskbook['primary_task'], 
                                    name=taskbook.get('name', None),
                                    inventory=taskbook['inventory'], 
                                    **taskbook.get('kwargs',{}))

    #stop timer
    taskbook['elapsed_time'] = datetime.now() - start_time

    # Post Jobs 
    for job in taskbook['post_jobs']:
        job(taskbook)



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--device', type=str, nargs='+', required=False)
    parser.add_argument('--group', type=str, nargs='+', required=False)
    parser.add_argument('--role', type=str, nargs='+', required=False)
    parser.add_argument('--taskbook', type=str, required=True)
    args = parser.parse_args()

    main(args)
