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

payload = {
    "name": "ams01-leaf-11",
    "device_type": "74cf95a8-4233-46b9-a740-fba4f5dc88d3",
    "status": "9f38bab4-4b47-4e77-b50c-fda62817b2db",
    "role": "869267d8-7d75-4bd3-8a9e-5e6adcf200f6",
    "tenant": "1f7fbd07-111a-4091-81d0-f34db26d961d",
    "platform": "f48fd9e2-45c5-4c2f-aa54-28964edb3e1e",
    "location": "9e39051b-e968-4016-b0cf-63a5607375de",
}

devices_url = "https://demo.nautobot.com/api/dcim/devices/"

# adds ams01-leaf-11 to the location AMS01
r = session.post(devices_url, data=json.dumps(payload))

interface_url = "https://demo.nautobot.com/api/dcim/interfaces/"

device_id = r.json()["id"]

payload = {
    "device": device_id,
    "name": "Loopback0",
    "status": "9f38bab4-4b47-4e77-b50c-fda62817b2db",
    "type": "virtual",
}

# adds Loopback0 to ams01-leaf-11
r = session.post(interface_url, data=json.dumps(payload))

interface_id = r.json()["id"]

ip_address_url = "https://demo.nautobot.com/api/ipam/ip-addresses/"

payload = {
    "address": "10.11.128.11/32",
    "namespace": "733d191a-4067-4215-90a8-814bcfe28f03",
    "tenant": "1f7fbd07-111a-4091-81d0-f34db26d961d",
    "type": "host",
    "status": "9f38bab4-4b47-4e77-b50c-fda62817b2db",
    "dns_name": "leaf-11.ams01.atc.nautobot.com",
}

# creates IP
r = session.post(ip_address_url, data=json.dumps(payload))

ipaddr_id = r.json()["id"]

ipam_url = "https://demo.nautobot.com/api/ipam/ip-address-to-interface/"

payload = {"interface": interface_id, "ip_address": ipaddr_id}

# assigns IP to Loopback0 on ams01-leaf-11
r = session.post(ipam_url, data=json.dumps(payload))
