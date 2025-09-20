import numpy as np

class PILA:
    __pila: np
    __dimencion: int
    __tope: int
    def __init__(self, dimension = 5):
        self.__tope = -1
        self.__pila = np.empty(5, dtype = int)
        self.__dimencion = dimension
    def insertar(self, num):
        resultado = 0
        if self.vacia():
            self.__tope += 1
            self.__pila[self.__tope] = num
            resultado = num
        else: 
            if self.vacia():
                print("Lista llena")
            else:
                self.__tope += 1
                self.__pila[self.__tope] = num
                resultado = num
        return resultado 
    def suprimir(self):
        resultado = 0
        if self.vacia():
            print("La lista esta vacia")
        else:
            resultado = self.__pila[self.__tope]
            self.__tope -= 1
        return resultado
    def llena(self):
        return self.__tope == self.__dimencion -1 
    def vacia(self):
        return self.__tope == -1
    def getPrimero(self):
        return self.__pila[self.__tope]
    def recorrer(self):
        i = self.__tope
        while i >= 0:
            print(self.__PILA[i])
            i -= 1

