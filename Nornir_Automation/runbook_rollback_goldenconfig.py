from nornir import InitNornir
from nornir_scrapli.tasks import (send_command, send_config, send_interactive)
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yml")

def golden_config(task):
    cmds = [("copy running-config flash:xcrs", "Destination filename"), ("\n", f"{task.host}#")]
    task.run(task = send_interactive, interact_events = cmds)

results = nr.run(task= golden_config)
print_result(results)

def rollback_config(task):
    task.run(task = send_command, command = "configure replace flash:xcrs force")

results = nr.run(task= rollback_config)
print_result(results)