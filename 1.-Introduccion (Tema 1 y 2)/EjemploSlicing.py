#Muestra los caracteres en un rango 

caracteres = "123787563627435ygdf"

primeros_10_caracteres = caracteres[0:10]
segunos_10_caracteres = caracteres[10:20]
todos_los_caracteres = caracteres[:]

#Lo mismo pero con array(listas)

dias = ['lunes','martes','miercoles','jueves','viernes','sabado','domingo']
diarios = dias[0:5]
fin_de_semana = dias[5:]

#seleciona x puestos despues del primero 

impares = ['uno','dos','tres','cuatro','cinco','seis','siete','ocho','nueve','dies']
numinpares = impares[0::2]

print(primeros_10_caracteres)
print(segunos_10_caracteres)
print(todos_los_caracteres)
print(diarios)
print(fin_de_semana)
print(numinpares)
