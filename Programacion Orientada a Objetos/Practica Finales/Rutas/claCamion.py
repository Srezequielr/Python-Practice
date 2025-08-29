from claVehiculo import Vehiculo

class Camion(Vehiculo):
    __capMaxCarga: int
    __cantTransportada: int
    def __init__(self, patente, modelo, costoXKm, cantDias, capMaxCarga, cantTransportada):
        super().__init__(patente, modelo, costoXKm, cantDias)
        self.__capMaxCarga = capMaxCarga
        self.__cantTransportada = cantTransportada
    def getCapMaxCarga(self):
        return self.__capMaxCarga
    def getCantTransportada(self):
        return self.__cantTransportada
    def calcCostoAd(self):
        resultado = 0
        if(self.getCantTransportada() > 4500):
            resultado = 5 + self.getCostoXKm() / 100
        else:
            resultado = 2 + self.getCostoXKm() / 100
        return resultado
    def __str__(self):
        return f"""Patente: {self.getPatente()}
                   Modelo: {self.getModelo()}
                   Costo por kilometro: {self.getCostoXKm()}
                   Cantidad de dias: {self.getCantDias()}
                   Capacidad max de pasajeros: {self.getCapMaxCarga()}
                   Cantidad de pasajeros Transportados: {self.getCantTransportada()}"""
        