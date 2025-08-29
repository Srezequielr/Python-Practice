class Carrera:
    __id: int
    __nombre: str
    __titulo: str
    __duracion: str
    __nivel: str
    __idFacultad: int 
    def __init__(self, id, nombre, titulo, duracion, nivel, idFacultad):
        self.__id = id
        self.__nombre = nombre
        self.__titulo = titulo
        self.__duracion = duracion
        self.__nivel = nivel
        self.__idFacultad = idFacultad
    def obtNombre(self):
        return self.__nombre
    def obtIdFacultad(self):
        return self.__idFacultad
    def obtIdCarrera(self):
        return self.__id
    
        