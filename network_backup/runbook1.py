from nornir import InitNornir
from nornir_scrapli.tasks import send_command, send_configs, send_commands, send_commands_from_file, send_configs_from_file
from nornir_utils.plugins.tasks.files import write_file
from nornir_utils.plugins.functions import print_result
from datetime import date
import pathlib

nr = InitNornir(config_file= "config.yml")

def backup_config(task):
    cmds = ["show run", "show version"]
    for cmd in cmds:
        config_dir = "config-archive"
        date_dir = config_dir + "/" + str(date.today())
        command_dir = date_dir + "/" + cmd
        pathlib.Path(config_dir).mkdir(exist_ok= True)
        pathlib.Path(date_dir).mkdir(exist_ok= True)
        pathlib.Path(command_dir).mkdir(exist_ok= True)
        output = task.run(task = send_command, command = cmd)
        task.run(task = write_file, content = output.result, filename = command_dir + f"/{task.host}.txt")

results = nr.run(task= backup_config, name= "creating Back up config")
# print_result(results)
