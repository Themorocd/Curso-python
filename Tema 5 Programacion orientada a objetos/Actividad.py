#Actividad para practicar lo aprendido 
#Crea una clase que represente una cuenta bancaria.
#Debe contener el nombre del cliente, el número de cuenta y el saldo. 
#Asimismo, debe permitir ingresar o retirar dinero de la cuenta.
#Además, debe disponer de un método para mostrar por pantalla los datos de la cuenta. 
#De modo que, instancia una cuenta, realiza una operación de ingreso, otra de retirada de dinero y muestra los datos de la cuenta para finalizar.


#Definicion de clase

class cuenta_bancaria:
    
    def __init__(self, numero, nombre_cliente, saldo):
        self.numero = numero
        self.nombre_cliente = nombre_cliente
        self.saldo = saldo
    
    def ingresar_dinero(self,importe):
        self.saldo = self.saldo + importe
    def retirar_dinero(self,importe):
        self.saldo = self.saldo - importe
    def mostrar_datos(self):
        print("Numero de cuenta:",self.numero)
        print("Nombre del cliente:",self.nombre_cliente)
        print("Saldo:",self.saldo)

#Instanciacion

cuenta_10 = cuenta_bancaria("ES2114650100341520876293","Yolanda Alonso",1200)

#Utilizacion de los metodos

cuenta_10.ingresar_dinero(250)
cuenta_10.retirar_dinero(25)
cuenta_10.mostrar_datos()
    