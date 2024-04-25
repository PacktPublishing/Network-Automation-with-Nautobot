import requests
import json

payload = {}

headers = {
    "Content-Type": "application/json",
    "Authorization": "Token aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
}

devices_url = "https://demo.nautobot.com/api/dcim/devices/"

session = requests.Session()
session.headers.update(headers)

response = session.get(devices_url)
