import requests
import json

meraki_api_key = "29eb58d73cc5f731afa67fa8e2aac2aa44084949"
#meraki_api_key = "76d52810510e74aac786e0b34dcb52c42d3fac0b"
url = "https://api.meraki.com/api/v1/organizations"
headers = {
    "X-Cisco-Meraki-API-Key" : meraki_api_key,
}

orgs = requests.get(url,headers=headers)
while 400 <= orgs.status_code <= 499:
    print("La API key " + meraki_api_key + " es invalida")
    meraki_api_key = input("Ingresar una nueva API key: ")
    headers = {
    "X-Cisco-Meraki-API-Key" : meraki_api_key,
    }
    orgs = requests.get(url,headers=headers)

orgs = orgs.json()
c = 0
for org in orgs:
    if org["name"] == "Devnet-GroupGamma":
        print("La organizacion Devnet-GroupGamma ya existe.")
        print("El ID de la organizacion es: " + org["id"])
        c += 1
        id = org["id"]
        break
if c == 0:
    print("No existe la organizacion Devnet-GroupGamma. Se creara a continuacion.")
    params = '''{ "name": "Devnet-GroupGamma" }'''
    headers = {
        "Content-Type" : "application/json",
        "Accept" : "application/json",
        "X-Cisco-Meraki-API-Key" : meraki_api_key
    }
    res = requests.request('POST', url, headers=headers, data = params)
    while res.status_code == 403:
        print("Su llave no esta autorizada para realizar cambios en el sistema Meraki")
        meraki_api_key = input("Ingresar una nueva API key: ")
        headers = {
        "Content-Type" : "application/json",
        "Accept" : "application/json",
        "X-Cisco-Meraki-API-Key" : meraki_api_key,
        }
        res = requests.request('POST', url, headers=headers, data = params)
    res = res.json()
    print("Organizacion creada exitosamente")
    print("ID de la nueva organizacion creada: " + res["id"])
    id = res["id"]


url = "https://api.meraki.com/api/v1/organizations/" + id + "/networks"
headers = {
    "X-Cisco-Meraki-API-Key" : meraki_api_key,
}

networks = requests.get(url,headers=headers)
networks = networks.json()
c = 0
for network in networks:
    if network["name"] == "Network-Gamma":
        print("La red Network-Gamma ya existe.")
        print("El ID de la red es: " + network["id"])
        c += 1
        netId = network["id"]
        break
if c > 0:
    x = input("Desea eliminar la red Network-Gamma?: (y/n) ")
    if x == "y":
        url = "https://api.meraki.com/api/v1/networks/" + netId
        payload = None
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "X-Cisco-Meraki-API-Key": meraki_api_key
        }
        response = requests.request('DELETE', url, headers=headers, data = payload)
        print("Red Network-Gamma con ID " + netId + " ha sido eliminada.")

if c == 0:
    print("No existe la red Network-Gamma. Se creara a continuacion.")
    params = '''{
    "name": "Network-Gamma",
    "timeZone": "America/Los_Angeles",
    "disableMyMerakiCom": false,
    "type": "Virtual Appliance",
    "productTypes" : [
        "appliance",
        "switch",
        "wireless"
    ]
    }'''
    headers = {
        "Content-Type" : "application/json",
        "Accept" : "application/json",
        "X-Cisco-Meraki-API-Key" : meraki_api_key
    }
    res = requests.request('POST', url, headers=headers, data = params)
    while res.status_code == 403:
        print("Su llave no esta autorizada para realizar cambios en el sistema Meraki")
        meraki_api_key = input("Ingresar una nueva API key: ")
        headers = {
        "Content-Type" : "application/json",
        "Accept" : "application/json",
        "X-Cisco-Meraki-API-Key" : meraki_api_key,
        }
        res = requests.request('POST', url, headers=headers, data = params)
    res = res.json()
    print("Red creada exitosamente")
    print("ID de la nueva red creada: " + res["id"])
    netId = res["id"]

