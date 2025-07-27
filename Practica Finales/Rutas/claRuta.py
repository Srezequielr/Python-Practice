class Ruta:
    __cod: int
    __destino: str
    __distancia: int
    __asignada: bool
    def __init__(self, cod, destino, distancia, asignada):
        self.__cod = cod
        self.__destino = destino
        self.__distancia = distancia
        self.__asignada = asignada
    def getCod(self):
        return self.__cod
    def getDestino(self):
        return self.__destino
    def getDistancia(self):
        return self.__distancia
    def getAsignada(self):
        return self.__asignada
    def asigRuta(self):
        self.__asignada = True
