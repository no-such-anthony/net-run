# net-run

A micro Nornir/Ansible like automation poc tool.  

- Inventory (inc inheritance) and threading are similar to Nornir.
- The tasks in a taskbook are similar to Ansible Playbook but in a Python dict.
- Connection methods (but not limited to): Netmiko 4, Scrapli, Napalm, ncclient.

As this is just a proof of concept example there is no docco or unit testing.  

There is more work be done with the taskbook concept, filtering, and how to present the output.  The general idea being a taskbook contains the primary task (mandatory), the subtask list, connection_method/connection_key (eg netmiko, napalm, etc), run_mode (async, threads (default), serial), num_workers.  The tasks/subtasks that are here are just simple examples for code verification.

Taskbook argument is a file location, of which the parent directory is automatically appended to sys.path.  Any directories in taskbook['append_paths'] will also be appended to sys.path.

Example usage for a taskbook using Netmiko 4 SSH with list of subtasks
- python net-run.py --taskbook taskbooks/netmiko1.py --device r1 r3 --role roleA

Example usage for taskbook using Scrapli SSH2 with list of subtasks
- python net-run.py --taskbook taskbooks/scrapli1.py --group group1

Example usage for taskbook using Scrapli asyncssh with list of subtasks (run_mode = 'async')
- python net-run.py --taskbook taskbooks/async1.py --device r2 r4 --group group1

Example usage for taskbook using Napalm with list of subtasks
- python net-run.py --taskbook taskbooks/napalm1.py --group group1

Example usage for taskbook using ncclient with list of subtasks
- python net-run.py --taskbook taskbooks/netconf1.py --device core1

Example usage for a taskbook with a custom primary_task and no subtasks
- python net-run.py --taskbook taskbooks/custom1.py

Example usage for a taskbook with a custom primary_task with subtasks and run_mode = 'serial' (loop)
- python net-run.py --taskbook taskbooks/custom2.py

Example usage for a taskbook with a custom restconf task
- python net-run.py --taskbook taskbooks/restconf1.py --device core2

To install Netmiko 4
- pip install git+https://github.com/ktbyers/netmiko.git@develop

