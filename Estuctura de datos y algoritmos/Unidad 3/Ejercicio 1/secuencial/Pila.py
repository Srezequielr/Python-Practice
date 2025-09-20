import numpy as np

class PILA:
    __PILA: np.array
    __tope: int
    def __init__(self, dimension = 5):
        self.__dimension = dimension
        self.__tope = -1
        self.__PILA = np.empty(self.__dimension, dtype = int)
    def insertar(self, num):
        resultado = 0
        if self.estaVacia():
            self.__tope += 1
            self.__PILA[self.__tope] = num
            resultado = num
        else: 
            if self.estaLlena():
                print("Lista llena")
            else:
                self.__tope += 1
                self.__PILA[self.__tope] = num
                resultado = num
        return resultado 
    def suprimir(self):
        resultado = 0
        if self.estaVacia():
            print("La lista esta vacia")
        else:
            resultado = self.__PILA[self.__tope]
            self.__tope -= 1
        return resultado   
    def recorrer(self):
        i = self.__tope
        while i >= 0:
            print(self.__PILA[i])
            i -= 1
    def estaVacia(self):
        return self.__tope == -1
    def estaLlena(self):
        return self.__tope == self.__dimension - 1
