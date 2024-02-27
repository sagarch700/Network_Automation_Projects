from nornir import InitNornir
from nornir_scrapli.tasks import (send_command, send_config, send_interactive)
from nornir_utils.plugins.functions import print_result
import getpass
import sys
import os

nr = InitNornir(config_file="config.yml")

# Password security using getpass module
password = getpass.getpass()
nr.inventory.defaults.password = password

# Password security along with multiple passwords for each groups and hosts
test_group1_pwd = getpass.getpass(prompt= "Enter the test group1 pwd: ")
test_group2_pwd = getpass.getpass(prompt= "Enter the test group2 pwd: ")
r3_pwd = getpass.getpass(prompt= "Enter the host R3 pwd: ")

nr.inventory.groups["test_group1"].password = test_group1_pwd
nr.inventory.groups["test_group2"].password = test_group2_pwd
nr.inventory.hosts["R3"].password = r3_pwd

# Username from command-line argument
nr.inventory.defaults.username = sys.argv[1]
nr.inventory.defaults.username = os.getenv("USERNAME")
nr.inventory.defaults.password = os.getenv("PASSWORD")


def golden_config(task):
    cmds = [("copy running-config flash:xcrs", "Destination filename"), ("\n", f"{task.host}#")]
    task.run(task = send_interactive, interact_events = cmds)

results = nr.run(task= golden_config)
print_result(results)

def rollback_config(task):
    task.run(task = send_command, command = "configure replace flash:xcrs force")

results = nr.run(task= rollback_config)
print_result(results)