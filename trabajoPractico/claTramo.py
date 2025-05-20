class Tramo:
    __origen: str
    __destino: str
    __distancia: float
    __patente: str
    def __init__(self, origen = "", destino = "", distancia = 0, patente = ""):
        self.__origen = origen
        self.__destino = destino
        self.__distancia = distancia
        self.__patente = patente
    def obtOrigen(self):
        return self.__origen
    def obgDestino(self):
        return self.__destino
    def obtDistancia(self):
        return self.__distancia
    def obtPatente(self):
        return self.__patente
    def __str__(self):
        return f"- Origen: {self.__origen}.\n- Destino: {self.__destino}.\n- Distancia: {self.__distancia}."
    def __gt__(self, otro):
        return self.__distancia > otro.__distancia    