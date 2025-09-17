import numpy as np

class Cola:
    __cola: np.array
    __max: int
    __ui: int
    __pr: int
    __cant: int
    def __init__(self, dimencion = 5):
        self.__max = dimencion
        self.__ui = 0
        self.__pr = 0
        self.__cant = 0
        self.__cola = np.empty(dimencion, dtype = int)
    def vacia(self):
        return self.__cant == 0
    def llena(self):
        return self.__cant == self.__max
    def insertar(self, numero):
        result = None
        if(self.llena()):
            print("La cola esta llena.")
        else:
            self.__cola[self.__ui] = numero
            self.__ui = (self.__ui + 1) % self.__max
            self.__cant += 1
            result = numero
        return result
    def suprimir(self):
        result = None
        if(self.vacia()):
            print("La cola esta vacia.")
        else:
            result = self.__cola[self.__pr]
            self.__cant -= 1
            self.__pr = (self.__pr + 1) % self.__max
        return result
    def recorrer(self):
        if(self.vacia()):
            print("La cola esta vacia.")
        else:
            i = self.__pr
            for _ in range(self.__cant):
                print(self.__cola[i])
                i = (i + 1) % self.__max