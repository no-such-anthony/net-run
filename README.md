# net-run

A micro Nornir/Ansible like automation poc tool.  

- Inventory (inc inheritance) and threading are similar to Nornir.
- The tasks in a taskbook are similar to Ansible Playbook but in a Python dict.
- Connection methods (but not limited to): Netmiko 4, Scrapli, Napalm, ncclient.

As this is just a proof of concept example there is no docco or unit testing.  

There is more work be done with the taskbook idea, filtering, and how to present the output.  The general idea being a taskbook contains the primary task (mandatory), the subtask list, and the connection method.  The tasks/subtasks that are here are just simple examples for code verification.

Example usage for a taskbook using Netmiko 4 SSH with list of subtasks
- python net-run.py --taskbook netmiko1 --device r1 r3 --role roleA

Example usage for taskbook using Scrapli SSH2 with list of subtasks
- python net-run.py --taskbook scrapli1 --group group1

Example usage for taskbook using Scrapli asyncssh with list of subtasks
- python net-run.py --taskbook async1 --device r2 r4 --group group1

Example usage for taskbook using Napalm with list of subtasks
- python net-run.py --taskbook napalm1 --group group1

Example usage for taskbook using ncclient with list of subtasks
- python net-run.py --taskbook netconf1 --device core1 core2

Example usage for a taskbook with a custom primary_task and no subtasks
- python net-run.py --taskbook custom1

Example usage for a taskbook with a custom primary_task with subtasks
- python net-run.py --taskbook custom2

Example usage for a taskbook with a custom restconf task
- python net-run.py --taskbook restconf1

To install Netmiko 4
- pip install git+https://github.com/ktbyers/netmiko.git@develop




