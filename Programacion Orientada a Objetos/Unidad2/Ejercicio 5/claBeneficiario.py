class Beneficio:
    __dni: str
    __nombre: str
    __apellido: str
    __carrera: str
    __facultad: str
    __anio: int
    __promedio: float
    __idBeca: int
    def __init__(self, dni = 0, nombre = "", apellido ="", carrera = "", facultad = "", anio = 0, promedio = 0, idBeca = 0):
        self.__dni = dni
        self.__nombre = nombre
        self.__apellido = apellido
        self.__carrera = carrera
        self.__facultad = facultad
        self.__anio = anio
        self.__promedio = promedio
        self.__idBeca = idBeca
    