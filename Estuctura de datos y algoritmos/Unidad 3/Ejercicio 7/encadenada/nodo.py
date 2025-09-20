class Nodo:
    __tLlegada: int
    __cantPag: int
    __siguiente: object
    def __init__(self, tiempo, cantPag):
        self.__tLlegada = tiempo
        self.__cantPag = cantPag
        self.__siguiente = None
    def getSiguiente(self):
        return self.__siguiente
    def getCanPag(self):
        return self.__cantPag
    def getTllegada(self):
        return self.__tLlegada
    def setCantPag(self, paginas):
        self.__cantPag = paginas
    def setSiguiente(self, doc):
        self.__siguiente = doc