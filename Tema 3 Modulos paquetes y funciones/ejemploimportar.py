import calculadora

operaciones = calculadora.numero_operaciones
resultado = calculadora.sumar(3,8)

print(resultado)

#Otra forma de importar
# import calculadora as calc   // se usa "as" para darle un alias al modulo, tambien se puede usar para dar un alias a un elemento individual del modulo
# from calculadora import sumar,restar   // se usa from para importar una parte del modulo en concreto 
# from calculadora import *     // o el contenido entero

#Para evitar ejecuciones no deseadas de código, se puede incluir una estructura condicional cuyo contenido se va a ejecutar solo en el caso en el que el módulo al que pertenece sea el módulo que se ha ejecutado.
#Módulos, paquetes y funciones
#La estructura se muestra a continuación. La variable __name__ contiene el nombre del módulo o la cadena __main__ si hay sido el primer módulo en ejecutarse.


#ejemplo: 
# if __name__ == '__main__':
    #codigo de inicio
    
    