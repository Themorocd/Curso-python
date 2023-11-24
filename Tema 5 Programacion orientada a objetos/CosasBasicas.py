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