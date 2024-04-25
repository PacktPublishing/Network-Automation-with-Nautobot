import requests
import json

payload = {}

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "Authorization": "Token aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
}

session = requests.Session()
session.headers.update(headers)

payload = {"data": {}}

run_job_url = (
    "https://demo.nautobot.com/api/extras/jobs/Device Software Validation Report/run/"
)
r = session.post(run_job_url, data=json.dumps(payload))

print(r.status_code)
