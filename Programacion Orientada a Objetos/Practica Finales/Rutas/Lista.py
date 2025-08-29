from Nodo import Nodo

class Lista:
    __comienzo: None
    __actual: Nodo
    __indice:  int
    __tope: int
    def __init__(self):
        self.__comienzo = None
        self.__actual = None
    def __iter__(self):
        return self
    def __next__(self):
        if (self.__indice == self.__tope):
            self.__actual = self.__comienzo
            self.__indice = 0
            raise StopIteration
        else:
            self.__indice += 1
            dato = self.__actual.getSiguiente()
            self.__actual = self.__actual.getSiguiente()
            return dato
    def agregarNodo(self, vehiculo):
        nodo = Nodo(vehiculo)
        nodo.setSiguiente(self.__comienzo)
        self.__comienzo = nodo
        self.__actual = nodo
        self.__tope += 1
    def getLongitud(self):
        return self.__tope
    def buscarVehiculo(self, numMat):
        aux = self.__comienzo
        encontrado = False
        resultado = None
        
        while aux != None and not encontrado:
            if(numMat == aux.getVehiculo().getPatente()):
                encontrado = True
                resultado = aux.getVehiculo().getPatente()
            else:
                aux = aux.getSiguiente()
            i += 1
        return resultado
