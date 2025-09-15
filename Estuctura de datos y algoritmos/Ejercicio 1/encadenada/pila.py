from nodo import Nodo

class Pila:
    __cabeza: object
    __cant: int
    def __init__(self):
        self.__cabeza = None 
        self.__cant = 0
    def insertar(self, numero):
        nuevoNodo = Nodo(numero)
        nuevoNodo.setSiguiente(self.__cabeza)
        self.__cabeza = nuevoNodo
        self.__cant += 1
        return numero
    def vacia(self):
        return self.__cant == 0
    def suprimir(self):
        if(self.vacia()):
            print("La pila esta vacia.")
        else:
            nodo = self.__cabeza
            self.__cabeza = nodo.getSiguiente()
            self.__cant -= 1
            return nodo
    def recorrer(self):
        actual = self.__cabeza
        while actual is not None:
            print(actual.getDato())
            actual = actual.getSiguiente()