
class Ficha_empleado:
    def __init__(self, nombre = None,apellidos = None):
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = None
        self.cui = None
        self.direccion = None
        self.__antiguedad = None

    def set_antiguedad(self,antiguedad):
        self.__antiguedad = antiguedad

    def get_antiguedad(self):
        return self.__antiguedad

    def sueldo(self):
        return (1000 + self.__antiguedad*25)

class Ficha_fabricacion(Ficha_empleado):
    #Sobrescribiendo el constructor
    def __init__(self, articulos_mes):
        #Llamando al constructor de la clase padre
        super().__init__()
        self.__articulos_mes = articulos_mes

    def get_articulos_mes(self):
        return self.__articulos_mes

    def set_articulos_mes(self, articulos_mes):
        self.__articulos_mes = articulos_mes

    def incrementar_articulos(self, suma):
        self.__articulos_mes += suma

class Ficha_tecnico(Ficha_empleado):
    def __init__(self):
        super.__init__()
        self.__estrellas = 0

    def set_estrellas(self, estrellas):
        self.__estrellas = estrellas

    def get_estrellas(self):
        return self.__estrellas

    def incrementar_estrellas(self):
        self.__estrellas += 1

    def disminuir_estrellas(self):
        self.__estrellas -= 1

class Ficha_comercial(Ficha_empleado):
    def __init__(self):
        super.__init__()
        self.__cliente_principal = None
        self.__numero_clientes = None

    def set_cliente_principal(self, cliente):
        self.__cliente_principal = cliente

    def set_numero_clientes(self, numero):
        self.__numero_clientes = numero

    def get_cliente_principal(self):
        return self.__cliente_principal

    def get_numero_clientes(self):
        return self.__numero_clientes


