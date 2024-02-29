from nornir import InitNornir
from nornir_napalm.plugins.tasks import napalm_configure
from nornir_utils.plugins.functions import print_result
from tqdm import tqdm

nr = InitNornir(config_file="config.yml")

def random_configs(task):
    task.run(task = napalm_configure, filename = "random_config.txt", dry_run = True)

results = nr.run(task= random_configs)
print_result(results)
