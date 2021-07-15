import requests
import json

# Suppress HTTPS warnings
from urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)


def bytesAsJSON(bytes):
	return json.dumps(json.loads(bytes), indent=2)


def restconf1(device):

    print(device['name'])

    response = requests.get(
                    url = f"https://{device['restconf']['host']}/restconf/data/Cisco-IOS-XE-native:native/interface/GigabitEthernet=1",
                    auth = (device['restconf']['username'], device['restconf']['password']),
                    headers = {
                        'Accept': 'application/yang-data+json'
                    },
                    verify = False)


    # return either a dictionary with at least a 'result' key/value pair, or simply a string/integer
    output = bytesAsJSON(response.content)

    return output


# taskbook dictionary needs at least a primary_task pointing to a callable function
taskbook = {}
taskbook['primary_task'] = 'taskbooks.restconf1.restconf1'
