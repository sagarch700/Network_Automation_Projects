from nornir import InitNornir
from nornir_napalm.plugins.tasks import napalm_get
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yml")

def pull_info(task):
    result = task.run(task = napalm_get, getters = ["get_interfaces"])

results = nr.run(task = pull_info)

# results["hostname"]
# results["hostname"][0] to check for the pass or fail status

# Parsing the data is tricky, so follow the below steps
# nornir gives and aggregated result, to get the result of a specific device use its hostname and [1] .result converts the output to string
parsing = results["R4"][1].result
# get the dict of all the interfaces
interface_parse = parsing["get_interfaces"]
# get the outptut of a specific interface you like
interface_data = interface_parse["GigabitEthernet0/0/0/0"]
print(interface_data)
# print_result(results)


