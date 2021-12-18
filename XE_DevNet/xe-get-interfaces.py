#***************
#xe-get-interfces.py
#*************
import json
import requests
requests.packages.urllib3.disable_warnings()

api_url = "https://10.10.0.254/restconf/data/ietf-interfaces:interfaces"

headers = { "Accept": "application/yang-data+json",
 "Content-type":"application/yang-data+json"
 }

basicauth = ("admin", "cisco")
resp = requests.get(api_url, auth=basicauth, headers=headers, verify=False)
print(resp)

response_json = resp.json()
print(response_json)

print(json.dumps(response_json, indent=4))
