from nornir import InitNornir
from nornir_scrapli.tasks import send_commands_from_file, send_commands, send_configs, send_configs_from_file
from nornir_utils.plugins.functions import print_result
from tqdm import tqdm

nr = InitNornir(config_file="config.yml")

def random_configs(task, progress_bar):
    task.run(task = send_configs_from_file, file = "random_config.txt")
    progress_bar.update()

with tqdm (total = len(nr.inventory.hosts)) as progress_bar:
    results = nr.run(task= random_configs, progress_bar = progress_bar)

print_result(results)
