class ProgramaCapacitacion:
    __nombre: str
    __codigo: str
    __duracion: int
    def __init__(self, nombre = "", codigo = "", duracion = 0):
        self.__nombre = nombre
        self.__codigo = codigo
        self.__duracion = duracion
    def obtNombre(self):
        return self.__nombre
    def obtCodigo(self):
        return self.__codigo
    def obtDuracion(self):
        return self.__duracion