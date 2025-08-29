from claMascota import Mascota

class Cliente:
    __dni: str
    __nombre: str
    __apellido: str
    __Mascotas: list
    def __init__(self, dni, nombre, apellido):
        self.__dni = dni
        self.__nombre = nombre
        self.__apellido = apellido
        self.__Mascotas = []
    def obtDni(self):
        return self.__dni
    def obtNombre(self):
        return self.__nombre
    def obtApellido(self):
        return self.__apellido   
    def agregarMascota(self, dniCliente, nombre, especie, edad):
        mascota = Mascota(dniCliente, nombre, especie, edad)
        self.__Mascotas.append(mascota)
        print("Mascota agregada con exito")