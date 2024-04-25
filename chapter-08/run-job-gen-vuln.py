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

payload = {"data": {"published_after": "1975-01-01"}}

run_job_url = "https://demo.nautobot.com/api/extras/jobs/Generate Vulnerabilities/run/"
r = session.post(run_job_url, data=json.dumps(payload))

print(r.status_code)
