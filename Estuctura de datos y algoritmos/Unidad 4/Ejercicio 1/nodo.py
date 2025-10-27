class Nodo:
    __dato: int
    __izq: object
    __der: object
    def __init__(self, dato):
        self.__dato = dato
        self.__izq = None
        self.__der = None
    def setDato(self, dato):
        self.__dato = dato
    def getDato(self):
        return self.__dato
    def setIzq(self, nuevaHoja):
        self.__izq = nuevaHoja
    def setDer(self, nuevaHooja):
        self.__der = nuevaHooja
    def getIzq(self):
        return self.__izq
    def getDer(self):
        return self.__der
    def grado(self):
        grado = 0
        if(self.__izq):
            grado += 1
        if(self.__der):
            grado += 1
        return grado