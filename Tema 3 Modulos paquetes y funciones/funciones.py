def saludar (nombre):
    print("Hola",nombre)
    


def convertir (nombre):
    nombre_convertido = nombre.upper()
    return nombre_convertido

convertir("andres")
saludar("Andres")


def sumar (s1, s2=1):#aunque s2 tenga ya un valor predefinido este se puede sustituir si se agregan luego otros valores
    resultado =s1 + s2
    return resultado

ingresos_totales = sumar(10000, 20000)# si pongo solo 10.000 el resultado sera 10.001 
print("Los ingresos totales ascienden a", ingresos_totales)