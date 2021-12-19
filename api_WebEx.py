# █▓▒░ [ Create a Room | https://developer.webex.com/docs/api/v1/rooms/create-a-room ] # Crear una Sala
# Nota: La URL de nuestro token de acceso personal solo tendra una duración de doce horas [ Your Personal Access Token | https://developer.webex.com/docs/getting-started ]
# Crear un ROOM con el nombre “Devnet-GroupGamma”
import requests
import json 

choice = input("¿Desea utilizar el token de Webex codificado de forma predeterminada? (Y/n) ")
if choice == "n":
    accessToken = input("¿Cuál es su token de acceso? ")
    accessToken = "Bearer " + accessToken
else:
	accessToken = "Bearer YzRiZjQ2ZmMtY2ZhYS00ODRkLWEyZjUtMWMwZjBmYzZlYThkNDRhOGY4YTQtNjkx_PF84_d3558e03-2933-4d83-8021-b115db9045d4"
url = "https://webexapis.com/v1/rooms"
headers = {
    "Authorization": accessToken,
    "Content-Type": "application/json"
}
params={'title': 'Devnet-GroupGamma'}

room_resp = requests.post(url, headers=headers, json=params)
room_resp_json = room_resp.json()
print("\n█▓▒░ La sala se creo correctamente...\n")
#print(json.dumps(room_resp_json, indent=4))  #Salida de los datos comentada (Si descomentamos esta línea podremos mostrar los datos de la sala) 


# Obteniendo los datos del administrador
# ---------------------------------------
url = 'https://webexapis.com/v1/people/me'
headers = {
    'Authorization': accessToken,
    }
admin_resp = requests.get(url, headers=headers)
admin_resp_json = admin_resp.json()
#print(json.dumps(res.json(), indent=4))
# ---------------------------------------


# En este ROOM deben estar incluidos todos los integrantes del grupo
#print(f"\nPara incluir al resto de los integrantes, se usara el identificador de la sala previamente creado: {room_resp_json['id']}")
room_id = room_resp_json['id']
#person_email_00 = "testunknown0@gmail.com"
person_email_01 = "markituxfor@gmail.com"
person_email_02 = "rivmont.diego@gmail.com"
person_email_03 = "nflores1019@gmail.com"


url = "https://webexapis.com/v1/memberships"
headers = {
    "Authorization": accessToken,
    "Content-Type": 'application/json'
}
#params_00 = {'roomId': room_id, 'personEmail': person_email_00}
#memberships_resp_00 = requests.post(url, headers=headers, json=params_00)
#memberships_resp_00_json = memberships_resp_00.json()

params_01 = {'roomId': room_id, 'personEmail': person_email_01}
memberships_resp_01 = requests.post(url, headers=headers, json=params_01)
memberships_resp_01_json = memberships_resp_01.json()

params_02 = {'roomId': room_id, 'personEmail': person_email_02}
memberships_resp_02 = requests.post(url, headers=headers, json=params_02)
memberships_resp_02_json = memberships_resp_02.json()

params_03 = {'roomId': room_id, 'personEmail': person_email_03}
memberships_resp_03 = requests.post(url, headers=headers, json=params_03)
memberships_resp_03_json = memberships_resp_03.json()

print("\n█▓▒░ Los integrantes se incluyeron correctamente en la sala...\n")
#print(json.dumps(memberships_resp_00_json, indent=4))       #Salida de los datos comentada (Si descomentamos esta línea podremos mostrar los datos del nuevo miembro)
#print(json.dumps(memberships_resp_01_json, indent=4))       #Salida de los datos comentada (Si descomentamos esta línea podremos mostrar los datos del nuevo miembro)
#print(json.dumps(memberships_resp_02_json, indent=4))       #Salida de los datos comentada (Si descomentamos esta línea podremos mostrar los datos del nuevo miembro)
#print(json.dumps(memberships_resp_03_json, indent=4))       #Salida de los datos comentada (Si descomentamos esta línea podremos mostrar los datos del nuevo miembro)

print(f"\n█▓▒░ El identificador de la sala es: {room_resp_json['id']}\n")
print(f"\n█▓▒░ Los correos de los integrantes de la sala Devnet-GroupGamma son: {admin_resp_json['userName']}, {memberships_resp_01_json['personEmail']}, {memberships_resp_02_json['personEmail']} y {memberships_resp_03_json['personEmail']}\n")

# Luego debe enviar un mensaje al Room con la ruta del contenedor en el Docker Hub.
access_token = 'NDZlZmE1ZTEtYzI5My00MWUwLTgwMzMtODY4MTMxNjQwOWMzYzUwODZiOGMtN2Ex_PF84_d3558e03-2933-4d83-8021-b115db9045d4'
room_id = room_resp_json['id']
message = 'Hola **DevNet Associates**, la ruta del contenedor se encuentra en el siguiente enlace: [Docker Hub] (https://hub.docker.com/layers/183375727/darklyn3r/docker-groupgamma/latest/images/sha256-c7025d56ec6b5deda970caa70a83b82cf628758175b6be8dc4abdca76afd99d6?context=repo)'
url = 'https://webexapis.com/v1/messages'
headers = {
    'Authorization':  accessToken,
    'Content-Type': 'application/json'
}
params = {'roomId': room_id, 'markdown': message}
res = requests.post(url, headers=headers, json=params)
# print(res.json())


print(f"\n█▓▒░ Su mensaje se publico correctamente, por favor revise su sala... \n")
