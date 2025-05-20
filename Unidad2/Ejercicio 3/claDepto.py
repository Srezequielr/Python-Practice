class Departamento:
    __nombre = str
    __codigo = int
    def __init__(self, nombre = "", codigo = 0):
        self.__nombre = nombre
        self.__codigo = codigo
    def obtNombre(self):
        return self.__nombre    
    def obtCodigo(self):
        return self.__codigo