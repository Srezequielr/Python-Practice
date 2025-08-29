class Mascota: 
    __dniCliente: str
    __nombre: str
    __especie: str
    __edad: int
    def __init__(self, dniCliente, nombre, especie, edad):
        self.__dniCliente = dniCliente
        self.__nombre = nombre
        self.__especie = especie
        self.__edad = edad
    def obtDniCliente(self):
        return self.__dniCliente
    def obtNombre(self):
        return self.__nombre
    def obtEspecie(self):
        return self.__especie
    def obtEdad(self):
        return self.__edad