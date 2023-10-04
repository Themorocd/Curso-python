#Esto es un diccionario:
diccionario = {"pan":"break","cebolla":"onion","agua":"water"}
#Los metodos keys, values y items proporcionan la lista de claves(keys), valores(values) y de elementos(items) de un diccionario 
#Recorrer un diccionario mediante un for
for clave in diccionario.keys():
    print(clave)
#Para poder acceder a todo el diccionario tenemos que formar el for con 2 elementos
for clave, valor in diccionario.items():
    print(clave,valor)
#el acceso a los elementos no se realiza a través de posición sino de clave
traduccion = diccionario["pan"]
print(traduccion)
