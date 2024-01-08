#Declaracion basica de una clase

class Factura:
    pass#pass se usa para que una clase vacia no proboque un error por estar vacio

#Los metodos se declaran dentro del bloque de codigo de la clase como una funcion comun, con la palabra def
#obligatoriamente, todos los metodos deben de recibir al menos un parametro denominado self

class Vehiculo:
    def __init__ (self):
        self.motor_arrancado = False
    def arrancar(self):
        self.motor_arrancado = True
    def parar(self):
        self.motor_arrancado = False

#El modificador de acceso más restrictivo convierte en privado al atributo o al método sobre el que se utiliza, permitiendo el acceso solo al propio objeto.
# Estos modificadores (y algunos más) no existen en Python. En Python, todos los atributos y métodos de una clase son públicos. 
#No obstante, se puede ocultar un atributo para “simular” que su visibilidad es privada. 
# Para ello, basta con incluir uno o dos guiones bajos antes de su nombre.

class Vehiculo:
    def __init__ (self):
        self._codigo = 12345
        self.motor_arrancado = False
    def _modificar_codigo(self, nuevo_codigo):
        self._codigo = nuevo_codigo
    def arrancar(self):
        self.motor_arrancado = True
    def parar(self):
        self.motor_arrancado = False

#Metodo __init__:

class Vehiculo:
    vida_util = 10
    def __init__(self,marca,modelo,cilindrada):
        self.__codigo = 12345
        self.marca = marca
        self.modelo = modelo
        self.cilindrada = cilindrada
        self.motor_arrancado = False

##Pagina 9/23 del tema 5

def __del__(self):
    self.motor_arrancado = False
    
    
#Instanciacion de objetos

micoche = Vehiculo("kia","ceed",1600)

#Asi se ejecutan sus metodos

micoche.motor_arrancado #Acceso al valor del atributo arrancado
micoche.arrancar() #Ejecucion del metodo arrancar
micoche.parar() #Ejecucion del metodo parar


#Ejemplo de constructor con dos instanciaciones diferentes:

class Cliente:
    def __init__(self,nombre,estado_civil="desconocido"):
        self.nombre = nombre
        self.estado_civil = estado_civil

cliente1 = Cliente("Dwayne Johnson")
cliente2 = Cliente("Charlize Theron", "soltera")

#Herencia y herencia multiple

class Motocicleta(Vehiculo):
    
    def __init__(self, marca, modelo,cilindrada,numero_ruedas):
        super() .__init__(marca,modelo,cilindrada)
        self.numero_ruedas = numero_ruedas

#Para indicar que una clase hereda de mas de una clase, se debe de indicar estas entre parentesis

#class gato (mamifero,felino):
    
#Polimorfismo

class vehiculo: 
    
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    def arrancar(self):
        print("Arrancando vehiculo...")
    
class Motocicleta(vehiculo):
    
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)
    def arrancar(self):
        print("Arrancando motocicleta...")

class Automovil(vehiculo):
    
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)
    def arrancar(self):
        print("Arrancando automovil...")

john_deere = vehiculo("John Deere","Serie 6M")
suzuki = Motocicleta("Suzuki","SV650X 2023")
kia = Automovil("Kia","Ceed")
john_deere.arrancar()
suzuki.arrancar()
kia.arrancar()

#Atributos y metodos de clase

class vehiculo: 
    vida_util = 10
    
    def __init__(self):
        self.__codigo = 12345
        self.motor_arrancado = False
    def __modificar_codigo(self,nuevo_codigo):
        self.__codigo = nuevo_codigo
    def arrancar(self):
        self.motor_arrancado = True
    def parar(self):
        self.motor_arrancado = False
    
    @classmethod
    def incrementar_vida_util(cls):
        cls.vida_util +=1   


#Un decorador en Python es una anotación que se antepone a la declaración
# de un método o función para añadirle una funcionalidad concreta. Los nombres de los decoradores comienzan por el símbolo arroba (@). En el siguiente código se muestra la definición del método calcular_potencia al que se le aplica el decorador @staticmethod: 

@staticmethod
def calcular_potencia(numero_cilindros,cilindrada):
    caballos = 0.08 * numero_cilindros
    (cilindrada/numero_cilindros) ** 0.6
    return caballos
vehiculo.calular_potencia(1400,4)

#Clases abstractas e interfaces 

from abc import ABC, abstractmethod

class Calculadora(ABC):
    
    def __init__(self):
        self.resultado = 0
    @abstractmethod
    def sumar(self,sumando1, sumando2):
        pass

class CalculadoraDecimal(Calculadora):
    
    def reiniciar(self):
        self.resultado = 0
        
    def sumar(self, sumando1, sumando2):

        self.resultado = sumando1 + sumando2

calculadora = CalculadoraDecimal()
calculadora.reiniciar()
calculadora.sumar(12,11)
print(calculadora.resultado)

#Clases internas

class CV(object):
    
    def __init__(self, nombre, direccion, idioma, nivel):
        self.nombre = nombre
        self.direccion = direccion
        self.experiencias = []
        self.idioma = CV.Idioma(idioma, nivel)
        
    class Idioma():
        
        def __init__(self, idioma, nivel)-> None:
            self.idioma = idioma
            self.nivel = nivel

micv = CV("Andrés José","Marín Pascualvaca","Ingles",4)
print("Idioma:",micv.idioma.idioma)
print("Nivel:",micv.idioma.nivel)

        
    