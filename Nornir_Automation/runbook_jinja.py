from nornir import InitNornir
from nornir_scrapli.tasks import send_configs
from nornir_utils.plugins.functions import print_result
from nornir_jinja2.plugins.tasks import template_file
from nornir_utils.plugins.tasks.data import load_yaml

nr = InitNornir(config_file = "config.yml")

# This is with static variables
def test_template(task):
    result = task.run(task = template_file, template = "ospf.j2", path = "templates")
    task.host["opsf"] = result.result
    rendered = task.host["ospf"]
    configuration = rendered.splitlines()
    task.run(task = send_configs, configs = configuration)

results = nr.run(task= test_template)
print_result(results)

# This is to load variables and then using jinja2 templates using those variables loaded

def load_vars(task):
    data = task.run(task = load_yaml, file = f"./host_vars/{task.host}.yml")
    task.host["facts"] = data.result
    snmp_test_template(task)

def snmp_test_template(task):
    template = task.run(task = template_file, template = "snmp.j2", path = f"{task.host.platform}-templates")
    task.host["snmp_config"] = template.result
    rendered = task.host["snmp_config"]
    configuration = rendered.splitlines()
    task.run(task = send_configs, configs = configuration)


