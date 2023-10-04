#Escribe un programa que pida una palabra al usuario y le muestre la traducción a partir de los datos contenidos en un diccionario.

diccionario = {"coche":"car","vino":"wine","cielo":"sky"}
palabra = input("Escribe una palabra para obtener su traduccion:<br>")
if (palabra in diccionario.keys()):
    print("La traduccion de",palabra,"es",diccionario[palabra])
else:
    print("Esta palabra no esta disponible")