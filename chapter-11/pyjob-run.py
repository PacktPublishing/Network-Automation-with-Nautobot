import os
import requests
import json

import pynautobot

url = f"{os.getenv('NAUTOBOT_URL')}/api/extras/jobs/Command Runner/run/"

# Get the UUID of the device name
nautobot = pynautobot.api(
    url=os.getenv("NAUTOBOT_URL"), token=os.getenv("NAUTOBOT_TOKEN"), verify=False
)

device_id = nautobot.dcim.devices.get(name="jcy-bb-01.infra.ntc.com").id

payload = json.dumps(
    {
        "data": {
            "device": device_id,
            "user_name": "John Doe",
            "commands": ["show version"],
        }
    }
)


headers = {
    "Authorization": f'Token {os.getenv("NAUTOBOT_TOKEN")}',
    "Content-Type": "application/json",
    "accept": "application/json",
}

response = requests.request("POST", url, headers=headers, data=payload, verify=False)
print(json.dumps(response.json(), indent=2))
