#Actividad para practicar lo aprendido 
#Crea una clase que represente a un empleado. 
#Debe contener información sobre el nombre, el identificador y el salario. 
#Ahora, crea otra clase que represente a un empleado temporal y que herede de la clase anterior.
#Esta debe contener, además de la información heredada de la clase padre, el número de días de duración del contrato.
#Este número de días se puede incrementar a través de un método específico. 
#Seguidamente, incluye en la clase que representa al empleado temporal un método que muestre todos sus datos.
#Finalmente, crea un empleado temporal, incrementa el número de días de su contrato y muestra los datos por pantalla. 


#Definicion de la clase empleado

class Empleado: 
    
    def __init__(self, nombre, codigo, salario):
        self.nombre = nombre
        self.codigo = codigo
        self.salario = salario

#Definicion de la clase temporal

class Temporal(Empleado):
    
    def __init__(self, nombre, codigo, salario, duracion_contrado):
        super().__init__(nombre, codigo,salario)
        self.duracion_contrato = duracion_contrado
    def incrementar_duracion_contrato(self,incremento):
        self.duracion_contrato = self.duracion_contrato + incremento
    def mostrar_datos(self):
        print("Nombre:",self.nombre)
        print("Numero:",self.codigo)
        print("Salario:",self.salario)
        print("Duracion del contrato:",self.duracion_contrato)

#Instanciacion

empleado_temporal = Temporal("Yolanda Alonso","EMPTMP101",25000,180)

#Utilizacion de los metodos

empleado_temporal.incrementar_duracion_contrato(30)
empleado_temporal.mostrar_datos()
    
    