#Método format

#El método format se aplica a las cadenas de caracteres para realizar composiciones de cadenas que contienen partes variables, 
# dando así mayor flexibilidad a la construcción de cadenas

print(("El padre de {} se llama {}").format("Luke","Darth Vader"))

print(("El hijo de {1} se llama {0}").format("Luke","Darth Vader"))

print(("El padre de {hijo} se llama {padre}").format(padre = "Darth Vader", hijo = "Luke"))

