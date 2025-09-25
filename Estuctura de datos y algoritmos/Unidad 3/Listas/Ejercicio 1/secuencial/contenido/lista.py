import numpy as np

class Lista:
    __lista: np.array
    __max: int
    __ult: int
    def __init__(self, dimension = 8):
        self.__ult = 0
        self.__max = dimension
        self.__lista = np.empty(dimension, dtype = int)
    def llena(self):
        return self.__ult == self.__max - 1
    def vacia(self):
        return self.__ult == 0
    def insertar(self, numero):
        result = None
        if(self.llena()):
            print("Lista llena")
        else:
            pass