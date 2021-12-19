# █▓▒░ [ Create a Room | https://developer.webex.com/docs/api/v1/rooms/create-a-room ] # Crear una Sala
# Nota: La URL de nuestro token de acceso personal solo tendra una duración de doce horas [ Your Personal Access Token | https://developer.webex.com/docs/getting-started ]
# Crear un ROOM con el nombre “Devnet-GroupGamma”
import requests
import json 

accessToken = "NTUzODViNWYtYmQwMS00ZjhhLWI2YzItZjllYzc2NmY3YzJkZGQ2Y2M5MjItNmJl_P0A1_eb84e064-24b6-4877-a348-68ee377c32d0"

#choice = input("¿Desea utilizar el token de Webex codificado de forma predeterminada? (Y/n) ")
#if choice == "n":
#    accessToken = input("¿Cuál es su token de acceso? ")
#    accessToken = "Bearer " + accessToken
#else:
#accessToken = "YzRiZjQ2ZmMtY2ZhYS00ODRkLWEyZjUtMWMwZjBmYzZlYThkNDRhOGY4YTQtNjkx_PF84_d3558e03-2933-4d83-8021-b115db9045d4"
url = "https://webexapis.com/v1/rooms"

headers = {
    'Authorization' : 'Bearer {}'.format(accessToken),
    "Content-Type": "application/json"
}
res = requests.get(url,headers=headers)
while 400 <= res.status_code <= 499:
    print("El access token " + accessToken + " es invalido")
    accessToken = input("Ingresar un nuevo access token: ")
    headers = {
        'Authorization' : 'Bearer {}'.format(accessToken),
        "Content-Type": "application/json"
    }
    res = requests.get(url,headers=headers)

rooms = requests.get(url, headers=headers) 
rooms = rooms.json()
c = 0
for room in rooms["items"]:
    if room["title"] == "Devnet-GroupGamma":
        print("El Room con el nombre Devnet-GroupGamma ya existe.")
        print("El Room ID es: " + room["id"])
        room_id=room["id"]
        c += 1
        print("Estos son los correos de los integrantes del grupo:")
        url = "https://webexapis.com/v1/memberships?roomId=" + room["id"]
        members = requests.get(url, headers=headers)
        i = 1
        members = members.json()
        for member in members["items"]:
            print("Integrante " + str(i) + ": " + member["personEmail"])
            i += 1

if c == 0:
    params={'title': 'Devnet-GroupGamma'}
    room_resp = requests.post(url, headers=headers, json=params)
    room_resp_json = room_resp.json()
    #print(json.dumps(room_resp_json, indent=4))  #Salida de los datos comentada (Si descomentamos esta línea podremos mostrar los datos de la sala) 
    room_id=room_resp_json["id"]
    url = "https://webexapis.com/v1/rooms"
    person_email_00 = "darklyn3r@gmail.com"
    person_email_01 = "markituxfor@gmail.com"
    person_email_02 = "rivmont.diego@gmail.com"
    person_email_03 = "nflores1019@gmail.com"
    print("\n█▓▒░ La sala se creo correctamente...\n")
    url = "https://webexapis.com/v1/memberships"
    params_00 = {'roomId': room_id, 'personEmail': person_email_00}
    memberships_resp_00 = requests.post(url, headers=headers, json=params_00)
    memberships_resp_00_json = memberships_resp_00.json()

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

message = 'Hola **DevNet Associates**, la ruta del contenedor se encuentra en el siguiente enlace: [Docker Hub] (https://hub.docker.com/layers/183375727/darklyn3r/docker-groupgamma/latest/images/sha256-c7025d56ec6b5deda970caa70a83b82cf628758175b6be8dc4abdca76afd99d6?context=repo)'
url = 'https://webexapis.com/v1/messages'
params = {'roomId': room_id, 'markdown': message}
res = requests.post(url, headers=headers, json=params)

print(f"\n█▓▒░ Su mensaje se publico correctamente, por favor revise su sala... \n")