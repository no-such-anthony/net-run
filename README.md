# net-run

A micro Nornir/Ansible like automation poc tool built to experiment with Netmiko 4.

- Inventory (inc inheritance) and threading are similar to Nornir.
- The tasks in a taskbook are similar to Ansible Playbook but in a Python array.

As this is just a proof of concept example there is no docco or unit testing.  Still a lot of improvements to be done with the taskbook implementation.

Example usage
- python net-starter.py --device r2 --taskbook first1