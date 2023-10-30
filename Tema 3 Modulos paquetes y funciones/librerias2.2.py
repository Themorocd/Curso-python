#Instalacion de librerias ejemplo 2

import hashlib

algoritmo = hashlib.sha256()#obtiene una implementacion del algoritmo sha256

entrada = input("Introduce un texto: ")#solicita texto 

algoritmo.update(entrada.encode('utf-8'))#agrega el texto anterior al algoritmo

salida= algoritmo.digest()#aplica el algoritmo

print(salida)

