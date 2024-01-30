import re

nombre_fichero = input("introduzca el nombre del fichero:")
expresion_regular ="[a-zA-Z0-9]+\.py"
if(re.fullmatch(expresion_regular,nombre_fichero)):
    print("El nombre del fichero es correcto")
else:
    print("El nombre del fichero no es correcto")