from claHabitacion import Habitacion

class Hotel:
    __nombre = str
    __direccion = str
    __telefono = int
    __Habitaciones = list
    def __init__(self, nombre = "", direccion = "", telefono = 0 ):
        self.__nombre = nombre
        self.__direccion = direccion
        self.__telefono = telefono
        self.__Habitaciones = []
    def agregarHabitacion(self, numero, piso, tipo, precio, disponibilidad):
        habitacion = Habitacion(numero, piso, tipo, precio, disponibilidad)
        self.__Habitaciones.append(habitacion)
        print("Habitacion cargada con exito")
    def obtNombre(self):
        return self.__nombre
    def obtDireccion(self):
        return self.__direccion
    def obtTelefono(self):
        return self.__telefono
    def obtHabitaciones(self):
        return self.__Habitaciones
    def obtHabitacion(self, numHab): 
        encontrado = False
        i = 0
        resultado = False
        while not encontrado and i < len(self.__Habitaciones):
            if numHab == self.__Habitaciones[i].obtNumero():
                encontrado = True
                resultado = self.__Habitaciones[i]
            i += 1
        return resultado
    def __del__(self):
        print("Borrando datos")
        del self.__Habitaciones