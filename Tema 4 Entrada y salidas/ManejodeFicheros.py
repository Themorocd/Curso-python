#Python tiene mecanismos para manejar ficheros de manera sencilla, permitiendo realizar operaciones de lectura y 
#escritura con unas pocas líneas de código.  

# Modos de apertura:

#Imagen metodos de lectura

#El siguiente bloque de código abre el fichero datos.txt en modo escritura (w) y, posteriormente, lo cierra

fichero = open("datos.txt","w")
fichero.close()

#apertura y escritura de ficheros

fichero = open("datos.txt","w",encoding="utf-8")
fichero.write("Mi pelicula favorita es El Resplandor")
fichero.close()

#Ahora con sentencia with

with open ("datos.txt","w",encoding="utf-8") as fichero:
    fichero.write("Me gusta programar en Python")
    fichero.write("\n")
    fichero.write("Tambien me gusta programar en java")
    

#ejemplo con writelines:

peliculas = ["El resplandor,"," Alien,"," Tiburon,"," El Padrino "]
with open("datos.txt","w",encoding="utf-8") as fichero:
    fichero.writelines(peliculas)

#A continuación, se muestra el código que concatena sobre un fichero existente (el generado en el ejemplo anterior) un texto mediante la apertura en modo “a”:

with open("datos.txt","a",encoding="utf-8") as fichero:
    fichero.write(", Spiderman")
    
#El método read permite leer un fichero completo

fichero = open("cast.txt","w")
fichero.close()

with open("cast.txt","r",encoding="utf-8") as fichero:
    datos_leidos = fichero.read(5)
    
#El contenido de un fichero también se puede iterar utilizando un bucle for. 
# De esta manera, en cada iteración se va a leer una de las líneas del fichero. 
# El código que se muestra, a continuación, va a leer cada una de las líneas del fichero, 
# almacenando en cada iteración la línea leída en la misma, incluyendo el salto de línea del final:

with open("cast.txt","r",encoding="utf-8") as fichero:
    for participante in fichero:
        print("Participante:",participante)
        
#Por su parte, los métodos readline y readlines permiten leer una única línea o todas las líneas del fichero respectivamente. 

with open("cast.txt","r",encoding="utf-8") as fichero:
    print(fichero.readline())

#El siguiente código permite leer el fichero cast.txt con una única instrucción y obtener una lista con las diferentes líneas contenidas en él:

with open("cast.txt","r",encoding="utf-8") as fichero:
    print(fichero.readlines())
    
    #Me he quedado en la pagina 22/28 del tema 4