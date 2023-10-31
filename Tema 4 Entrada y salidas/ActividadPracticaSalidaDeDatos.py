
Empleados  = [("NASA","Peter Hugher","Responsable"),("NASA","Bhanu Sood","Responsable"),("Roscosmos","Dmitri Rogozin","Presidente")]
#Estos 3 print me crean el cuadrado que se ve por consola
print("*",end=" ")
print("*"*59,end=" ")
print("*")

for e in Empleados:
    
    print(f"* {e[0]:>10} * {e[1]:^20} * {e[2]:20}    *")#recorre el array y me lo pinta en consola 

#Me termina de cerrar el cuadrado
print("*",end=" ")# pone un * y un espacio al lado
print("*"*59,end=" ")#pone 59 *
print("*")