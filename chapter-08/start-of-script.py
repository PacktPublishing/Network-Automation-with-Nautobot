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
