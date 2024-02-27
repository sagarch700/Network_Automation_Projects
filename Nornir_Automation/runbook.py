from nornir import InitNornir
from nornir_scrapli.tasks import (
    get_prompt,
    send_command,
    send_config
)
from nornir_utils.plugins.functions import print_result

# show version output
nr = InitNornir(config_file="config.yml")
results = nr.run(task=send_command, command="show version")
print_result(results)

# # config ntp server
nr = InitNornir(config_file="config.yml")

def random_config(task):
    task.run(task= send_config, config = f"ntp server {task.host['ntp_server']}")

results = nr.run(task=random_config)
print(results)

