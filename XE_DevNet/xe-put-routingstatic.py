#===================================================================
#xe-loopback.py
import json
import requests
requests.packages.urllib3.disable_warnings()
#Se probo varios paths para entender la ruta correcta
#api_url = "https://10.10.0.254/restconf/data/ietf-routing:routing"
#api_url = "https://10.10.0.254/restconf/data/ietf-routing:routing-state"
#api_url = "https://10.10.0.254/restconf/data/ietf-routing:routing/routing-instance=default"
#api_url = "https://10.10.0.254/restconf/data/ietf-routing:routing/routing-instance/routing-protocols/routing-protocol=static-routes"
api_url = "https://10.10.0.254/restconf/data/ietf-routing:routing/routing-instance=default/routing-protocols"

headers = { "Accept": "application/yang-data+json",
 "Content-type":"application/yang-data+json"
 }

basicauth = ("admin", "cisco")
#resp = requests.get(api_url, auth=basicauth, headers=headers, verify=False)
yangConfig = {
    "ietf-routing:routing-protocols": {
        "routing-protocol": [
            {
                "type": "ietf-routing:static",
                "name": "1",
                "static-routes": {
                    "ietf-ipv4-unicast-routing:ipv4": {
                        "route": [
                            {
                                "destination-prefix": "0.0.0.0/0",
                                "next-hop": {
                                    "outgoing-interface": "Loopback4"
                                }
                            }
                        ]
                    }
                }
            }
        ]
    }
}

resp = requests.put(api_url, data=json.dumps(yangConfig), auth=basicauth, headers=headers, verify=False)



#print(resp)
#response_json = resp.json()
#print(response_json)
#print(json.dumps(response_json, indent=4))

if(resp.status_code >= 200 and resp.status_code <= 299):
    print("STATUS OK: {}".format(resp.status_code))
else:
    print("Error code {}, reply: {}".format(resp.status_code, resp.json()))
