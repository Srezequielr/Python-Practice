import numpy as np

class Lista:
    __lista: np.array
    __ult: int
    __max: int
    def __init__(self, dimencion = 10):
        self.__ult = 0
        self.__max = dimencion
        self.__lista = np.empty(dimencion, dtype = dimencion)
    def vacia(self):
        return self.__ult == 0
    def llena(self):
        return self.__ult == self.__max
    def insertar(self, pos, numero):
        result = None
        if(self.llena()):
            print("La lista esta llena.")
        elif(self.vacia()):
            print("Lista llena, insertando al comienzo...")
            self.__lista[self.__ult] = numero
            result = numero
        elif(not pos > self.__ult):
            for i in range(self.__ult, pos, -1):
                self.__lista[i] = self.__lista[i - 1]
            
        else:
            print("Posicion invalida.")
        
        return result
        
