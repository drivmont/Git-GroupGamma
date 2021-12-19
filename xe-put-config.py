#***************
# xe-put-config.py
# Creamos una interfaz loopback4
# Y creamos una ruta estatica por defecto
#*************

#Nos conectamos con el router, en relación a una interaz especifica
import json
import requests
requests.packages.urllib3.disable_warnings()

#Pedimos la IP del router, con el cual previamente se tiene conectividad
dirIP = input("Introduzca la direccion IP del router XE a trabajar: ")
interfaz = input("Introduzca la Interfaz que se añadira: ")

#api_url = "https://10.10.0.254/restconf/data/ietf-interfaces:interfaces/interface=Loopback4"
api_url = "https://"+dirIP+"/restconf/data/ietf-interfaces:interfaces/interface="+interfaz

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

#Ejecutamos el put para crear la interfaz
resp = requests.put(api_url, data=json.dumps(yangConfig), auth=basicauth, headers=headers, verify=False)
if(resp.status_code >= 200 and resp.status_code <= 299):
    print("STATUS OK: {}".format(resp.status_code))
    print("SE HA CREADO UNA INTERFAZ.")
else:
    print('Error. Status Code: {} \nError message: {}'.format(resp.status_code,resp.json()))
#Terminamos la creación de la interfaz

#Ahora desde el codido Verificación la creación
#Volvemos a ajustar la URL para consultar las interfaces
api_url = "https://10.10.0.254/restconf/data/ietf-interfaces:interfaces"

#Reusaremos la variable headers y basicauth 
resp = requests.get(api_url, auth=basicauth, headers=headers, verify=False)
print(resp)
print("CONFIRMEMOS LA CREACIÓN DE LA INTERFAZ.")
response_json = resp.json()
print(response_json)

print(json.dumps(response_json, indent=4))

#Ahora creemos la ruta estática

api_url = "https://10.10.0.254/restconf/data/ietf-routing:routing/routing-instance=default/routing-protocols"

#Reusaremos la variable headers y basicauth 

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

if(resp.status_code >= 200 and resp.status_code <= 299):
    print("STATUS OK: {}".format(resp.status_code))
    print("SE HA CREADO LA RUTA POR DEFECTO.")
else:
    print("Error code {}, reply: {}".format(resp.status_code, resp.json()))

print("VERIFIQUEMOS LA TABLA DE ENRUTAMIENTO")


#En este caso reusaremos las variables --> api_url, headers y basicauth 
#api_url = "https://10.10.0.254/restconf/data/ietf-routing:routing/routing-instance=default/routing-protocols"

resp = requests.get(api_url, auth=basicauth, headers=headers, verify=False)
print(resp)

response_json = resp.json()
print(response_json)

print(json.dumps(response_json, indent=4))

