class Paciente:
    __dni: int
    __nombre: str
    __unidad: str
    def __init__(self, dni, nombre, unidad):
        self.__dni = dni
        self.__nombre = nombre
        self.__unidad = unidad
    def getDni(self):
        return self.__dni
    def getNombre(self):
        return self.__nombre
    def getunidad(self):
        return self.__unidad
    def __str__(self):
        return (f"DNI: {self.__dni}, Nombre: {self.__nombre}, Unidad: {self.__unidad}")