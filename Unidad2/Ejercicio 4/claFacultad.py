class Facultad:
    __id: int
    __nombre: str
    __direccion: str
    __localidad: str
    __telefono: int
    def __init__(self, id, nombre, direccion, localidad, telefono):
        self.__id = id
        self.__nombre = nombre
        self.__direccion = direccion
        self.__localidad = localidad
        self.__telefono = telefono
    def obtNombre(self):
        return self.__nombre
    def obtIdFacultad(self):
        return self.__id