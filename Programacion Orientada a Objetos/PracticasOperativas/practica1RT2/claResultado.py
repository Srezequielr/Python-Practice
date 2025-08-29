##Julian riera

class Resultado:
    __fecha: str
    __idEquipoLocal: str
    __golesLocal: int
    __idEquipoVisitante: str
    __golesVisitante: int
    inscripcion = 45000
    def __init__(self, fecha = "", idEquipoLocal = 0, golesLocal = 0, idEquipoVisitante = 0, golesVisitante = 0):
        self.__fecha = fecha
        self.__idEquipoLocal = idEquipoLocal
        self.__golesLocal = golesLocal
        self.__idEquipoVisitante = idEquipoVisitante
        self.__golesVisitante = golesVisitante
    def obtFecha(self):
        return self.__fecha
    def obtIdEquipoLocal(self):
        return self.__idEquipoLocal
    def obtIdEquipoVisitante(self):
        return self.__idEquipoVisitante
    def obtenerGolesLocal(self):
        return self.__golesLocal    
    def obtenerGolesVisitante(self):
        return self.__golesVisitante