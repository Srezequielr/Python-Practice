from claVehiculo import Vehiculo

class Automovil(Vehiculo):
    __maxPasajeros: int
    __cantPasTransportados: int
    __costAd = 5000
    def __init__(self, patente, modelo, costoXKm, cantDias, maxPasajeros, cantPasTransportados):
        super().__init__(patente, modelo, costoXKm, cantDias)
        self.__maxPasajeros = maxPasajeros
        self.__cantPasTransportados = cantPasTransportados
    def getMaxPasajeros(self):
        return self.__maxPasajeros
    def getCantPasTransportados(self):
        return self.__cantPasTransportados
    def getCostAd(cls):
        return cls.__costAd
    def calcCostoAd(self):
        return self.getCostAd() * self.getCantPasTransportados()
    def __str__(self):
        return f"""Patente: {self.getPatente()}
                   Modelo: {self.getModelo()}
                   Costo por kilometro: {self.getCostoXKm()}
                   Cantidad de dias: {self.getCantDias()}
                   Capacidad max de pasajeros: {self.getCantPasTransportados()}
                   Cantidad de pasajeros Transportados: {self.getCantPasTransportados()}"""
    
    
    