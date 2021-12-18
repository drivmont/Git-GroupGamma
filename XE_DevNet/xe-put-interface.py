#===================================================================
#resconf-put.py
import json
import requests
requests.packages.urllib3.disable_warnings()

api_url = "https://10.10.0.254/restconf/data/ietf-interfaces:interfaces/interface=Loopback4"
headers = {"Accept": "application/yang-data+json", "Content-type":"application/yang-data+json"}

basicauth = ("admin", "cisco")
#Se de cambiar la IP de la loopback4, pues estaria en la misma sub red 10.10.0.0/16
#El router nos rebota
#Por eso y por conveniencia cambiamos a otra sub red = 10.20.1.0/16, para mantener la idea de lo planteado
yangConfig = {
        "ietf-interfaces:interface": {
            "name": "Loopback4",
            "description": "DevNet Lab Group Gamma",
            "type": "iana-if-type:softwareLoopback",
            "enabled": True,
            "ietf-ip:ipv4": {"address": [{"ip": "10.20.1.4", "netmask": "255.255.0.0"}]},
            "ietf-ip:ipv6": {}
        }
}

resp = requests.put(api_url, data=json.dumps(yangConfig), auth=basicauth, headers=headers, verify=False)
if(resp.status_code >= 200 and resp.status_code <= 299):
    print("STATUS OK: {}".format(resp.status_code))
else:
    print('Error. Status Code: {} \nError message: {}'.format(resp.status_code,resp.json()))
#end of file
