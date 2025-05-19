class Colectivo:
    __patente: str
    __marca: str
    __modelo: float
    __capacidad: int
    __dniChof: int
    colectivo = 35
    def __init__(self, patente, marca, modelo, capacidad, dniChof):
        self.__patente = patente
        self.__marca = marca
        self.__modelo = modelo
        self.__capacidad = capacidad
        self.__dniChof = dniChof
    def obtPatente(self):
        return self.__patente
    def obtMarca(self):
        return self.__marca
    def obtModelo(self):
        return self.__modelo
    def obtCap(self):
        return self.__capacidad
    def obtDni(self):
        return self.__dniChof
    
        