import numpy as np

class Lista: 
    __ult: int
    __max: int
    __lista: np.array
    
    def __init__(self, dimencion = 20):
        self.__ult = 0
        self.__max = dimencion
        self.max = 0 
        self.__lista = np.empty(dimencion, dtype = int)
    def llena(self):
        return self.__ult == self.__max
    def vacia(self):
        return self.__ult == 0
    def insertar(self, contacto):
        if(self.llena()):
            raise Exception("La lista esta llena")
        
        pos = 0
        while pos < self.__ult and self.__elementos[pos] <= contacto:
            pos += 1

        for i in range(self.__ult, pos, -1):
            self.__elementos[i] = self.__elementos[i - 1]

        self.__elementos[pos] = contacto
        self.__ult += 1
    def suprimir(self, pos):
        if(self.vacia()):
            raise Exception("La lista esta vacia")
        
        pos -= 1
        if(pos < 0 and pos > self.__ult):
            raise IndexError("Posicion invalida")
    
    def buscar(self, valor):
        inicio = 0
        fin = self.__ult - 1
        while(inicio <= fin):
            medio = (inicio + fin) // 2
            if(self.__lista[medio] == valor):
                return medio
            
        