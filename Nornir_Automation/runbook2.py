from nornir import InitNornir
from nornir_scrapli.tasks import (
    get_prompt,
    send_command,
    send_commands,
    send_config,
    send_configs,
    send_commands_from_file,
    send_configs_from_file
)
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yml")

# Task-1: Show commands from a list
command_list = ["show ip int brief", "show version", "show run"]
def command_test(task): 
    task.run(task = send_commands, commands = command_list)

results = nr.run(task=command_test)
# Task-2: Show commands from a file
def show_command_test(task):
    task.run(task = send_commands_from_file, file = "random_commands.txt")

results = nr.run(task=show_command_test)
# print_result(results)

# Task-3: Send config
def send_config_test(task):
    task.run(task = send_config, config = "ip route 192.168.10.10 255.255.255.255 10.100.100.100")

results = nr.run(task = send_config_test)

# Task-4: Send configs
def send_configs_test(task):
    task.run(task = send_config, configs = ["router ospf 1", "network 0.0.0.0 255.255.255.255 area 0"])

results = nr.run(task = send_configs_test)

# Task-4: Send configs from a file
def send_configs_test_from_file(task):
    task.run(task = send_configs_from_file, file = "random_config.txt", dry_run = True)

results = nr.run(task = send_configs_test_from_file)
