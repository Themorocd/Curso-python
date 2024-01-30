#Generadores. La sentencia yield

#Un generador es una alternativa eficiente a estructuras de datos como listas y tuplas. 
# La diferencia fundamental es que el generador no almacena todos los datos en memoria, sino que los va generando bajo demanda

#Ejemplo 1. En el siguiente bloque de código, la función generador_numeros devuelve una lista con los números del 0 al 99.
# Esos 100 números están simultáneamente en memoria en el ámbito del bucle for que los procesa.

def generador_numeros():
    return list(range(100))
for i in generador_numeros():
    #la lista proporcionada por la funcion esta en memoria
    pass

#Ejemplo 2. En el siguiente bloque de código, la función generador_numeros es un generador que proporciona una lista con los números del 0 al 99 al bucle for. 
# La diferencia es que en el ámbito del bucle for que los procesa, la lista no está completa, sino únicamente el elemento que le ha proporcionado el generador.

def generador_numeros():
    for numero in list(range(100)):
        yield numero
    
for i in generador_numeros():
    #la lista proporcionada por la funcion esta en memoria
    pass

#Actividad para practicar lo aprendido 
#Construye un generador que proporcione los elementos de una tupla que contenga nombres de lenguajes de programación. Iterar por los elementos que proporciona el generador y mostrarlos por pantalla.

def obtener_lenguajes():
    lenguajes = ("Python","C","C++","Java","JavaScript","Cobol","Perl","Kotlin")
    for lenguaje in lenguajes:
        yield lenguaje
for lenguaje in obtener_lenguajes():
    print(lenguaje)