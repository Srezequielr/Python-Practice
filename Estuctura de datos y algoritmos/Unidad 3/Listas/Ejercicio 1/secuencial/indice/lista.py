import numpy as np

class Lista:
    __lista: np.array
    __ult: int
    __max: int
    def __init__(self, dimencion = 10):
        self.__ult = 0
        self.__max = dimencion
        self.__lista = np.empty(dimencion, dtype = int)
    def vacia(self):
        return self.__ult == 0
    def llena(self):
        return self.__ult == self.__max - 1
    def insertar(self, pos, numero):
        result = None
        if(self.llena()):
            print("La lista esta llena.")   
        elif(self.vacia()):
            print("Lista vacia, insertando al comienzo...")
            self.__lista[self.__ult] = numero
            self.__ult += 1
            result = numero
        elif(not pos - 1 > self.__ult):
            for i in range(self.__ult, pos - 1, -1):  # (Comienzo, Fin, Salto)
                self.__lista[i] = self.__lista[i - 1]
            self.__lista[pos - 1] = numero
            self.__ult += 1
            result = numero
        else:
            print("Posicion invalida.")
        return result
    def suprimir(self, pos):
        result = None
        if(self.vacia()):
            print("La lista esta vacia.")
        elif(not pos - 1 > self.__ult):
            result = self.__lista[pos - 1]
            for i in range(pos - 1, self.__ult):
                self.__lista[i] = self.__lista[i + 1]
            self.__ult -= 1
        else: 
            print("Posicion invalida.")
        return result
    def recorrer(self):
        i = 0
        while i < self.__ult:
            print(self.__lista[i])
            i += 1  
    def primerElemento(self):
        return self.__lista[0]
    def ultimoElemento(self):
        return self.__lista[self.__ult]
    def siguiente(self, p):
        if(p > self.__ult):
            print("Overflow")
        else:
            return self.__lista[p]
    def anterior(self, p):
        if (p - 2 < 0):
            print("Overflow")
        else:
            return self.__lista[p - 2]
    def buscar(self, dato):
        i = 0 
        encontrado = False
        result = None
        while not encontrado and i <= self.__ult:
            if(self.__lista[i] == dato):
                result = self.__lista[i]
                encontrado = True
        return result
        

        
    



        
