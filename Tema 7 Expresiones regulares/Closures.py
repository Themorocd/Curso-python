#Las closures son funciones anidadas que permiten encapsular funcionalidad. Una de sus características principales es que las funciones internas tienen acceso a las variables de las externas. 

#La llamada a la función generador proporcionando un 2, va a hacer que la función devuelta duplique el valor que se le pasa por parámetro.
# Del mismo modo, proporcionando un 3, la función devuelta multiplique por tres el valor que se le pasa por parámetro.

#Funcion externa
def generador(multiplicando):
    #Funcion interna
    def multiplicar(numero):
        return numero * multiplicando
    return multiplicar

duplicador = generador(2)
triplicador = generador(3)
print(duplicador(8))
print(triplicador(10))

#Actividad para practicar lo aprendido 
#Crea, utilizando closures, una función que detenga la ejecución del programa un determinado número de segundos. 
# Gracias al anidamiento de las funciones, se puede crear la función y ejecutarla cuando se desee, realizándose entonces la pausa. 
#Para hacer una pausa en la ejecución de un programa en Python, se puede utilizar el método sleep del módulo time. 
# Esta función recibe como parámetro un número entero y provoca la suspensión de la ejecución del programa, por ejemplo, sleep(3) va a detener la ejecución del programa 3 segundos.

from time import sleep

def hacer_pausa(segundos):
    def pausar():
        sleep(segundos)
        return pausar
    

temporizador_5=hacer_pausa(5)
print("Antes del temporizador")
temporizador_5()
print("despues del temporizador")