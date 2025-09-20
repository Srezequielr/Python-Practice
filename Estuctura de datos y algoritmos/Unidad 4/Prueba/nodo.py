class Nodo:
    __dato: int
    __izq: object
    __der: object
    def __init__(self, dato):
        self.__izq = None
        self.__der = None
        self.__dato = dato
    def getDato(self):
        return self.__dato
    def getIzq(self):
        return self.__izq
    def getDer(self):
        return self.__der
    def setIzq(self, izq):
        self.__izq = izq
    def setDer(self, der):
        self.__der = der