from clasePlanes import Plan

class Telefonia(Plan):
    __tipoLlamada: str
    __minutos: int
    def __init__(self, compania, duracion, cobertura, precioBase, tipoLlamada, minutos):
        super().__init__(compania, duracion, cobertura, precioBase)
        self.__tipoLlamada = tipoLlamada
        self.__minutos = minutos
    def getTipoLlamada(self):
        return self.__tipoLlamada
    def getMinutos(self):
        return self.__minutos
        