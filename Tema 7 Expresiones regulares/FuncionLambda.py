#Una función o expresión lambda es una función potencialmente anónima (sin nombre) de un solo uso. Son una alternativa compacta a las funciones tradicionales. Comienzan por la palabra reservada lambda

#En el siguiente bloque de código se define una función con la notación tradicional

def suma(s1,s2):
    return s1+s2
resultado = suma(3,8)

#Un código equivalente con funciones lambda se puede realizar de la siguiente manera:

sumador = lambda s1,s2: s1+s2
resultado = sumador(3,8)

#Uno de los usos habituales de las funciones lamdba consiste en incluirlas como parámetro de la función filter. 
# La función filter recibe como parámetro el nombre de una función y una colección de datos (una lista o una tupla, por ejemplo).

def es_calurosa(temperatura):
    if(temperatura>40):
        return True
    else:
        return False

temperaturas = (50,38,21,15,41,42,-5)

temperatura_calurosas = filter(es_calurosa,temperaturas)
temperatura_calurosas = list(temperatura_calurosas)
print(temperatura_calurosas)


#El mismo problema se puede resolver utilizando una función lambda, proporcionada como parámetro a la función filter. 
# En el siguiente ejemplo se muestra dicha solución:

temperaturas = (50,38,21,15,41,42,-5)
temperatura_calurosas = filter(lambda t:t>40,temperaturas)
temperatura_calurosas = list(temperatura_calurosas)
print(temperatura_calurosas)

#Actividad para practicar lo aprendido 
#Dada una tupla con nombres de fichero, obtener una lista con aquellos que tienen la extensión .jpg.  
# El método endswith de la clase str (string) permite averiguar si una cadena comienza o no por una subcadena: por ejemplo, “palacio”.endswith(“cio”) devuelve el valor True.
#La tupla de nombres de fichero de entrada es la siguiente:

ficheros = ("pelicula.jpg","novela.pdf","ropa.jpg","libro.gif","editor.png")
ficheros_jpg = filter(lambda fichero : fichero.endswith(".jpg"),ficheros)
ficheros_jpg = list(ficheros_jpg)
print(ficheros_jpg)
