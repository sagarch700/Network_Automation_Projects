from nornir import InitNornir
from nornir_netmiko.tasks import (
    netmiko_send_command,
    netmiko_send_config
)
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yml")

def command_test_netmiko_plugin(task):
    task.run(task = netmiko_send_command, command_string = "show interface description")

results = nr.run(task=command_test_netmiko_plugin)
print(results)

def command_test_file_netmiko_plugin(task):
    task.run(task = netmiko_send_config, config_file = "random_config.txt")

results = nr.run(task=command_test_file_netmiko_plugin)
print(results)
