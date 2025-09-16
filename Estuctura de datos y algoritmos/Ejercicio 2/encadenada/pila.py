from nodo import Nodo

class Pila:
    __cant: int
    __cabeza: object
    def __init__(self):
        self.__cabeza = None
        self.__cant = 0
    def vacia(self):
        return self.__cant == 0
    def insertar(self, numero): 
        nuevoNodo = Nodo(numero)
        nuevoNodo.setSiguiente(self.__cabeza)
        self.__cabeza = nuevoNodo
        self.__cant += 1
        return numero
    def suprimir(self):
        result = None
        if(self.vacia()):
            print("Lista vacia.")
        else:
            result = self.__cabeza
            self.__cabeza.setSiguiente(self.__cabeza.getSiguiente)
            self.__cant -= 1
        return result
    def recorrer(self):
        actual = self.__cabeza
        while actual is not None:
            print(actual.getDato())
            actual = actual.getSiguiente()