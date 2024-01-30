#El código Python capaz de obtener el documento JSON
import requests
import json

response = requests.get("https://localhost/motor/?marca=Ferrari")

status_code = response.status_code
if(status_code == 200):
    json_response={}
    json_response = json.loads(response.text)
    for coche in json_response:
        print(coche['id'])
        print(coche['nombre'])
        print(['descripcion'])
        
else:
    print("Ha ocurrido un error")
    
    
#Por su parte, una petición POST debe incluir los parámetros fuera de la dirección, algo permitido en las peticiones GET.

response = requests.post("https://localhost/motor/", params={'nombre': 'Ford Fiesta','descripcion': 'Es un vehiculo del segmento B'})
status_code = response.status_code
json_response={}
if(status_code == 200):
    json_response = json.loads(response.text)
    codigo = json_response['code']
    mensaje = json_response['message']