#ejemplo:
dias = ['lunes','martes','miercoles','jueves','viernes','sabado','domingo']
#Metodo append para agregar un elemento a la lista
dias.append("juernes")
#Seleccionar contenido de la lista y poder modificarlo y trabajar con el 
dias[5] = "sabado"
tercer_elemento = dias[2]
# for para recorrerlo 
for dia in dias:
    print(dia)
# con len obtengo el numero de elemento de la lista
longitud = len(dias)
# operadores in y not in para saber si un elemento se encuentra en la lista o no
existe = "martes" in dias #asigna true a existe
no_existe = "domingo " not in dias # asigna true a no_existe
# Metodos para las listas 
cesta = ['pan','leche','vinagre','cerveza','lechuga','apio','lechuga','cerveza']
#remove
cesta.remove("lechuga")#elimina la primera aparicion en la lista
# insert
cesta.insert(2,"Aceite")#inserta aceite en la segunda posicion de la lista
#reverse
cesta.reverse()#invierte el orden de la lista
#sort
cesta.sort()#ordena la lista por orden alfabetico 
#extend
carro = ['agua','refresco']
cesta.extend(carro)#agrega los elemento de carro a cesta
#index
posicion_cervesa = cesta.index("cerveza")#Obtiene la posicion de la primera aparicion de cerveza
#count
numero_cervesas = cesta.count("cerveza")#obtiene el numero de veces que aparece cerveza
#len
productos = len(cesta)#obtiene el numero de productos de la cesta
#max
mayor = max(cesta)#obtiene el ultimo elemento de la lista ordenada
#min
menor = min(cesta)#obtiene el primer elemento de la lista ordenada 