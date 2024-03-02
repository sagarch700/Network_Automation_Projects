from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_napalm.plugins.tasks import napalm_configure
from replace_tasks import replace_ospf

nr = InitNornir(config_file="config.yaml")


def replace_feature(task):

    config = replace_ospf(task)
    task.run(task=napalm_configure, configuration=config, replace=True)


result = nr.run(task=replace_feature)
# print_result(result)