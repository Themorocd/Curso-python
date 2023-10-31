
#el intérprete de Python va a entender las comillas del “no” como delimitadores de cadena, provocando un error: 

#frase = "Me dijo "no" y cerro la puerta"

#Para resolver este tipo de problemas se utilizan los caracteres de escape.
#el carácter de escape es \
    
print("El desconocido le dijo \"Ten cuidado\"")

print("El caracter \n genera un salto de linea")

#Para evitar que el carácter \n aparezca como tal y no sea interpretado como un salto de línea, se debe “escapar”, anteponiendo una barra \: 

print("El caracter \\n genera un salto de linea")

#Las cadenas crudas facilitan la creación de cadenas que contengan caracteres problemáticos

print(r"El caracter \n genera un salto de linea")

