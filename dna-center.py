import requests
import json
import sys
from requests.packages.urllib3.exceptions import InsecureRequestWarning

dnacip = "sandboxdnac.cisco.com"
username = "devnetuser"
password = "Cisco123!"

def get_X_auth_token(dnacip,username,password):
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
    post_uri = "https://"+dnacip+"/dna/system/api/v1/auth/token"
    try:
        r = requests.post(post_uri, auth=(username, password), verify=False)
        return r.json()["Token"]
    except:
        print ("Status: %s"%r.status_code)
        print ("Response: %s"%r.text)
        sys.exit()

def get_network_device(dnacip, headers, params, modifier):
    uri = "https://"+dnacip+"/dna/intent/api/v1/network-device"+modifier
    try:
        resp = requests.get(uri,headers=headers,params=params,verify = False)
        return resp
    except:
        print("Status: %s"%r.status_code)
        print("Response: %s"%r.text)
        sys.exit()

token = get_X_auth_token(dnacip, username, password)

headers = {"x-auth-token": token}
params=""
modifier="/count"
count = get_network_device(dnacip, headers, params, modifier)
count = json.dumps(count.json()["response"])
params=""
modifier=""
devices = get_network_device(dnacip, headers, params, modifier)
devices = devices.json()
print("DNA Center:")
print("-------------------------------------------------")
print("Cantidad de dispositivos: " + count)
print("-------------------------------------------------\n")
c = 1
for device in devices["response"]:
    print("Dispositivo " + str(c))
    print(" - Nombre del dispositivo: " + device["hostname"])
    print(" - Direccion IP de gestion: " + device["managementIpAddress"])
    print(" - Numero de serie: " + device["serialNumber"]+"\n")
    c += 1