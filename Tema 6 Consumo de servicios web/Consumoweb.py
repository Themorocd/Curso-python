#El puerto, en comunicaciones, es el identificador del punto de comunicación de uno de los elementos de la comunicación. 
# Los ordenadores disponen de un número importante, pero limitado, de puertos identificándose por un número entero.

#python -m http.server 80 

#Consumo de servicios web en python

import requests

response = requests.get("https://www.python.org/about/")
status_code = response.status_code
if(status_code == 200):
    codigo_html = response.text
    print(codigo_html)
else:
    print("Ha ocurrido un error")
    
    
#En el consumo de servicios web participan las peticiones HTTP y el procesado de los datos de salida que suelen estar en formato JSON. 
# En el siguiente ejemplo, se realiza una petición GET a un servicio web que retorna un documento JSON compuesto por un array de objetos caracterizados por los atributos id, nombre y descripción.
# Una posible respuesta proporcionada por el servicio web se muestra a continuación:


#tema 6 pagina 15/16 dia 8/01/2024