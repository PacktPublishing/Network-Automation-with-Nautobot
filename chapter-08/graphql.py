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

graphql_url = "https://demo.nautobot.com/api/graphql/"

query = """
query {
  devices(location: "AMS01") {
    name
    location {
      name
    }
  }
}
"""

payload = {"query": query}

r = session.post(graphql_url, data=json.dumps(payload))
