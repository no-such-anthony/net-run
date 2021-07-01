# net-run

A micro Nornir/Ansible like automation poc tool.  Uses Netmiko 4 SSH or Scrapli Asyncssh

- Inventory (inc inheritance) and threading are similar to Nornir.
- The tasks in a taskbook are similar to Ansible Playbook but in a Python array.

As this is just a proof of concept example there is no docco or unit testing.  

There is more work be done with the taskbook idea.  Easy to remove if not being used.

Example usage for Netmiko
- python net-run.py --taskbook first1 --device r1 --role roleA

Example usage for Scrapli
- python net-run.py --async --taskbook async1 --device r2 --group group2
