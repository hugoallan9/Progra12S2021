
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

#Instanciar la clase Ficha_empleado
jorge = Ficha_empleado('Jorge', 'Pérez')
jorge.set_antiguedad(10)
pedro = Ficha_empleado('Pedro', 'Rodríguez')
pedro.set_antiguedad(0)
#Acceder a los atributos de la clase
print('El nombre completo de jorge es', jorge.nombre, jorge.apellidos, 'su antiguedad es', jorge.get_antiguedad())
print('El salario de ', jorge.nombre, 'es', jorge.sueldo())
print('El nombre completo de pedro es', pedro.nombre, pedro.apellidos)
print('El salario de ', pedro.nombre, 'es', pedro.sueldo())
