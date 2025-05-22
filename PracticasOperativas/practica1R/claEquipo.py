# Julian Riera

class Equipo:
    __idEquipo: str
    __denominacion: str
    __presidente: str
    __puntos: int
    __golesAFavor: int
    __golesEnContra: int
    __diferenciaGoles: int
    def __init__(self, idEquipo = "", denominacion = "", presidente = "", puntos = 0, golesAFavor = 0, golesEnContra = 0, diferenciaGoles = 0):
        self.__idEquipo = idEquipo
        self.__denominacion = denominacion
        self.__presidente = presidente
        self.__puntos = puntos
        self.__golesAFavor = golesAFavor
        self.__golesEnContra = golesEnContra
        self.__diferenciaGoles = diferenciaGoles
    def obtDenominacion(self):
        return self.__denominacion
    def obtIdEquipo(self):
        return self.__idEquipo
    def obtPuntos(self):
        return self.__puntos
    def victoria(self):
        self.__puntos += 3
    def empate(self):
        self.__puntos += 1
    def cargarGolesAFavor(self, goles):
        self.__golesAFavor += goles
    def cargarGolesEnContra(self, goles):   
        self.__golesEnContra += goles
    def actualizarDiferenciaGoles(self):
        self.__diferenciaGoles = self.__golesAFavor - self.__golesEnContra
    def obtenerGolesAFavor(self):
        return self.__golesAFavor
    def obtenerGolesEnContra(self):
        return self.__golesEnContra
    def obtenerDiferenciaGoles(self):
        return self.__diferenciaGoles
    def __gt__(self, otro):
        if self.__puntos > otro.__puntos:
            return True
    
    