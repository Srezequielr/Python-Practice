class Nodo:
    __dato: int 
    __siguiente: object
    def __init__(self, dato):
        self.__dato = dato 
        self.__siguiente = None
    def getDato(self):
        return self.__dato
    def getSiguiente(self):
        return self.__siguiente
    def setSiguiente(self, nuevoNodo):
        self.__siguiente = nuevoNodo