import json

with open ("configuracion.json","r",encoding="utf-8") as fichero:
    datos = json.load(fichero)
    #Mostrar todos los datos contenidos en el fichero
    for clave, valor in datos.items():
        print(clave,":",valor)
    #Mostrar el valor de una clave concreta
    print("El esquema de color es",datos["esquema-color"])