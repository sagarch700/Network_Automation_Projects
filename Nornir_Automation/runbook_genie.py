from nornir import InitNornir
from nornir_scrapli.tasks import (
    send_command, 
    send_commands_from_file,
    send_commands,
    send_config,
    send_configs
)
from nornir_utils.plugins.functions import print_result
import ipdb
from rich import print as rprint


nr = InitNornir(config_file="config.yml")

def pull_structured_data(task):
    result = task.run(task = send_command, command = "show version")
    task.host["facts"] = result.scrapli_response.genie_parse_output()
    uptime = task.host["facts"]["uptime"]
    print(uptime)
    version_number = task.host["facts"]["software_version"]
    print(f"{task.host}: {version_number}")

results = nr.run(task= pull_structured_data)

def pull_cdp_data(task):
    result = task.run(task = send_command, command = "show cdp neighbor")
    task.host["facts"] = result.scrapli_response.genie_parse_ouptut()
    cdp_index = task.host["facts"]["cdp"]["index"]
    for num in cdp_index:
        local_intf = cdp_index[num]["local_interface"]
        remote_port = cdp_index[num]["port_id"]
        remote_device = cdp_index[num]["device_id"]
        # rprint(f"{task.host} {local_intf} is connected to {remote_device} {remote_port}")
        config_commands = [f"interface {local_intf}", f"description connected to {remote_device} via its {remote_port}"]
        task.run(task = send_configs, configs = config_commands )

results = nr.run(task = pull_cdp_data)
print_result(results)

# ipdb.set_trace()

''' once the code is run it moves to interactive debugger where you can parse the output
for eg: pp nr.inventory.hosts["R4"]["facts"]
        pp nr.inventory.hosts["R4"]["facts"]["version"]["uptime"]
'''
