import requests
import json

payload = {}

headers = {
    "Content-Type": "application/json",
    "Authorization": "Token aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
}

devices_url = "https://demo.nautobot.com/api/dcim/devices/?location=Jersey%20City"

session = requests.Session()
session.headers.update(headers)

all_devices = []

while devices_url is not None:
    response = session.get(devices_url)
    devices_url = response.json()["next"]
    all_devices.extend(response.json()["results"])

for device in all_devices:
    device["our_interfaces"] = []
    ip_url = f"https://demo.nautobot.com/api/ipam/ip-addresses?device={device['name']}"

    while ip_url is not None:
        ip_url_response = session.get(ip_url)
        ip_url = ip_url_response.json()["next"]
        device["our_interfaces"].extend(ip_url_response.json()["results"])

    for interface in device["our_interfaces"]:
        print(f"Device: {device['name']} has an IP Address {interface['address']}")
