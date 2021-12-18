#**********
# xe-get-routingtable.py 
#**********
import json
import requests
requests.packages.urllib3.disable_warnings()

#api_url = "https://10.10.0.254/restconf/data/ietf-routing:routing"
#api_url = "https://10.10.0.254/restconf/data/ietf-routing:routing-state"

#api_url = "https://10.10.0.254/restconf/data/ietf-routing:routing/routing-instance=default"

api_url = "https://10.10.0.254/restconf/data/ietf-routing:routing/routing-instance=default/routing-protocols"
#api_url = "https://10.10.0.254/restconf/data/ietf-routing:routing/routing-instance=default/routing-protocols/routing-protocol=static-routes"

headers = { "Accept": "application/yang-data+json",
 "Content-type":"application/yang-data+json"
 }

basicauth = ("admin", "cisco")
resp = requests.get(api_url, auth=basicauth, headers=headers, verify=False)
print(resp)

response_json = resp.json()
print(response_json)

print(json.dumps(response_json, indent=4))
