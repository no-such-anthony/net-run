# net-run

A micro Nornir/Ansible like automation poc tool.  Uses Netmiko 4 SSH or Scrapli Asyncssh

- Inventory (inc inheritance) and threading are similar to Nornir.
- The tasks in a taskbook are similar to Ansible Playbook but in a Python dict.

As this is just a proof of concept example there is no docco or unit testing.  

There is more work be done with the taskbook idea.

Example usage for a taskbook using Netmiko SSH with list of subtasks
- python net-run.py --taskbook first1 --device r1 r3 --role roleA

Example usage for taskbook using Scrapli asyncssh with list of subtasks
- python net-run.py --taskbook async1 --device r2 r4 --group group2

Example usage for a taskbook with a custom primary_task and no subtasks
- python net-run.py --taskbook custom1
