#Load a partir  de un documento JSON almacenado  en un fichero, 
# obtiene  una representacion del JSON en una estructura de datos de python(diccionario)
#----
#Loads a partir de un documento json almacenado en una cadena de caracteres, obtiene una representacion del JSON
# en una estructura de datos python(diccionario)
#----
#dump transforma un objeto pyhton en un documento json y lo almacena en un fichero
#----
#dumps transforma en un objeto python en un documento json y lo almacena en memoria

#DESDE FICHERO JSON
import json

with open("Estados.json","r", encoding="utf-8") as fichero:
    configuracion = json.load(fichero)
    print(configuracion)
    
#--------------DESDE CADENA-----------------


texto_json= """
[
    {"activado":true},
    {"activado":false},
    {"activado":null}
]

"""

print(json.loads(texto_json))

#-----Contruccion de un fichero JSON con DUMP----------------

estado = {"x":153,"y":80,"z":10,  "salud":35,  "superpoder":98}

with open("estado.json", "w",encoding="utf-8") as fichero_salida:

    json.dump(estado,fichero_salida)
    
                