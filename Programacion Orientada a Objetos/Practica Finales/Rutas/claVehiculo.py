from abc import ABC, abstractmethod

class Vehiculo(ABC):
    __patente: str
    __modelo: str
    __costoXKm: float
    __cantDias: int
    def __init__(self, patente, modelo, costoXKm, cantDias):
        self.__patente = patente
        self.__modelo = modelo
        self.__costoXKm = costoXKm
        self.__cantDias = cantDias
    def getPatente(self):
        return self.__patente
    def getModelo(self):
        return self.__modelo
    def getCostoXKm(self):
        return self.__costoXKm
    def getCantDias(self):
        return self.__cantDias
    @abstractmethod
    def calcCostoAd(self):
        pass
    def calcAlquiler(self):
        return (self.getCantDias() * self.getCostoXKm()) + self.calcCostoAd()

        
    