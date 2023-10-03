"""
nombre = "andres";
nombre
type (nombre)#Te dice el tipo de variable, es decir, si es int, str etc

aptop ="true";
type(aptop)


apto = True
type(apto)

apto = "hola me llamo andres"
type (apto)

nombre = "pepe"
dir()

isinstance (nombre,str)

del (nombre)
dir()

a=5
nombre="pepe"
programador = True
print (a,nombre,programador)

print(a,nombre,programador, sep="...")


print("pepe", end="--")


edad = input("Introduce tu edad: ")

print("tu edad es", edad)

print(type(edad))

edad = "51"
print(type(edad))

edad = int(edad)
print(type(edad))


edad = 23

if edad >= 18:
    print("eres mayor de edad")
else:
    print("eres menor")
    
edad_minima_laboral = 16
edad_maxima_laboral = 56

edad = int (input("introduce tu edad:"))

if(edad<edad_minima_laboral):
    print("No estas en edad laboral")
elif (edad>=edad_minima_laboral and edad<edad_maxima_laboral):
    print("Estas en edad laboral")
else:
    print("estas en edad de jubilarte")
    
Numero_secreto = 8
numero_candidato = 0

while numero_candidato != Numero_secreto:
    numero_candidato = int(input("Numero candidato:"))
    if(numero_candidato != Numero_secreto):
        print("El numero secreto no es", numero_candidato)
print("Enhorabuena, has descubierto el numero secreto")
"""
'''
for numero in range (5):
    print(numero)   
'''
'''    
for numero in range (5):
 if (numero == 3):
    print("Encontrado")
    break
 print(numero)
 '''
'''
try:
    resultado = 8/0
    print("Esta linea no se debe de ejecutar si ocurre un error")
except:
    print("Ha ocurrido un error")
    print("No se puede dividir entre 0")    
'''
'''
dividendo = int(input("introduce el dividendo"))
divisor = int(input("Introduce el divisor"))
try:
    resultado = dividendo/divisor
except:
    print("Ha ocurrido un error")
else:
    print("El resultado es", resultado)
finally:
    print("Fin de la ejecucion")
    '''

#Escribir ficheros:
# sin usar with:
fichero = open ("C:\\Users\\Andres\\git\\Curso-python\\salida-programa.txt",'w')
fichero.write("fichero escrito sin with")
fichero.close()

#Usando with:

with open ("C:\\Users\\Andres\\git\\Curso-python\\salida-programa.txt",'w') as fichero_with:
    fichero_with.write("Fichero escrito con with")
#Nota: no escribe el fichero por un error que no se como funciona, mirarlo(arreglado tenia que ponerle \\)

