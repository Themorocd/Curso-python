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
cesta.remove("Lechuga")#elimina la primera aparicion en la lista
# insert
cesta.insert(2,"Aceite")#inserta aceite en la segunda posicion de la lista
#reverse
cesta.reverse()#invierte el orden de la lista
#sort
cesta.sort()#ordena la lista por orden alfabetico 