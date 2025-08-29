from datetime import date
class Paciente:
    __dni: int
    __fecha: date
    __importe: float
    def __init__(self, dni, fecha, importe):
        self.__dni = dni
        self.__fecha = fecha
        self.__importe = importe
    def getDni(self):
        return self.__dni
    def getFecha(self):
        return self.__fecha
    def getImporte(self):
        return self.__importe
    def __str__(self):
        return (f"DNI: {self.__dni}, Fecha: {self.__fecha}, Importe: {self.__importe}")
        