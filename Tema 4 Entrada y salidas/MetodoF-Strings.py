#f-strings
#Los literales de cadenas con formato (f-strings o formatted string literals) permiten utilizar expresiones dentro de las cadenas.

print(F"Este texto incluye una expresion {2+5}.")

#Un formato puede ser un número entero. En este caso, el contenido de la expresión va a ocupar tantas posiciones 
# como indique el valor de dicho número completándose con espacios las posiciones vacías

print(F"Este texto incluye una expresion {2+5:10}.")

#También se pueden realizar acciones de alineación, mediante los símbolos > (derecha), < (izquierda) o ^ (centrada)

print(F"Este texto incluye una expresion {2+5:^10}.")

#Además, se puede especificar el tipo de dato que se quiere mostrar, indicando como formato el carácter “s” para cadenas de caracteres, 
# “d” para números enteros o “f”, para números decimales

print(F"Este texto incluye una expresion {2+5:f}.")