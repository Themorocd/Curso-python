#Ejemplo1Ejemplo 1. Creación de lista mediante la función range. La variable lista se construye con todos los elementos del rango:

lista = [i for i in range(10)]

lista

#Ejemplo 2. Creación de una lista a partir de una tupla. La variable días se construye con todos los elementos de la tupla: 


dias = ("viernes","sabado","domingo")

lista = [dia for dia in dias]

lista

#Ejemplo 3. Creación de una lista aplicando una transformación a los elementos de un rango. La variable lista se construye con el resultado de la ejecución de la función doble de cada elemento del rango: 

def doble(numero):
    return numero*2
    
lista = [doble(n) for n in range(5)]
lista

#Ejemplo 4. Creación de una lista de números pares menores que 10. La variable lista se construye con todos los elementos del rango cuyo resto de la división entre dos es 0 (números pares).

lista = [x for x in range(10) if x%2==0]
lista

#Ejemplo 5. Creación de una lista en la que los valores de las posiciones pares son los números correspondientes y los impares se sustituyen por la cadena “IMPAR”: 

lista = [x if x%2==0 else 'IMPAR' for x in range(10)]
lista

#Ejercicio Prueba
#Actividad para practicar lo aprendido 
#Crea una lista con los nombres que comiencen por la letra F utilizando compresión de listas. Para determinar si una cadena de caracteres comienza por una subcadena determinada se puede utilizar el método startswith de la clase str.
#La sentencia “película”.startswith(“pel”) devuelve el valor True mientras que “película”.startswith(“pol”) devuelve el valor False.
#Utiliza como datos de entrada para la comprensión de listas la siguiente tupla:
#nombres = ("Fermin","Jorge","Arturo","Luís","Fernando","Miguel Angel","German")

nombres = ("Fermin","Jorge","Arturo","Luís","Fernando","Miguel Angel","German")

nombre_f = [nombre for nombre in nombres if nombre.startswith("F")]

print(nombre_f)