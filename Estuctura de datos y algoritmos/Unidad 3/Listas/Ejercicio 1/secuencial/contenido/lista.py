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
        elif(self.vacia()):
            print("Lista vacia, insertando en la primer posicion...")
            self.__lista[self.__ult] = numero
            self.__ult += 1
            result = self.__lista[self.__ult - 1]
        else:
            i = 0
            while i < self.__ult and self.__lista[i] < numero:
                i += 1

            for j in range(self.__ult, i, -1):
                self.__lista[j + 1] = self.__lista[j]
            
            self.__lista[i] = numero
            self.__ult += 1
        return result
    def suprimir(self, pos):
        result = None
        if(self.vacia()):
            print("Lista vacia.")
        elif(self.__ult < pos - 1):
            print("Posicion invalida.")
        else:
            result = self.__lista[pos - 1]
            for j in range(pos - 1, self.__ult):
                self.__lista[j] = self.__lista[j + 1]
            self.__ult -=1 
        return result
    def recorrer(self):
        i = 0
        while i <= self.__ult:
            print(self.__lista[i])
            i += 1
    def buscar(self, elem):
        primero = 0 
        ultimo = self.__ult
        centro = None
        encontrado = False 
        result = None
        while not primero > ultimo and not encontrado:
            centro = (primero + ultimo) // 2
            if(self.__lista[centro] == elem):
                encontrado = True
                result = centro
            elif(self.__lista[centro] < elem):
                primero = centro - 1
            else:
                ultimo = centro + 1
        return result
    def recuperar(self, pos):
        result = None
        if(pos - 1 > self.__ult and pos - 1 < 0):
            print("Posicion invalida o lista vacia")
        else:
            result = self.__lista[pos]
        return result
    def primer(self):
        result = None
        if(self.vacia()):
            print("Lista vacia.")
        else:
            result = self.lista[0]
        return result
    def ultimo(self):
        result = None
        if(self.vacia()):
            print("La lista esta vacia.")
        else:
            result = self.__lista[self.__ult]
        return result
    def siguiente(self, pos):
        result = None
        if(pos - 2 > self.__ult and pos - 1 < 0):
            print("Posicion invalida")
        else:
            result = self.__lista[pos]
        return result
    def anterior(self, pos):
        result = None
        if(pos > self.__ult and pos - 2 < 0):
            print("Posicion invalida")
        else:
            result = self.__lista[pos - 2]
        return result
