from nodo import Nodo

class Cola:
    __cant: int
    __cabeza: object
    def __init__(self):
        self.__cant = 0
        self.__cabeza = None
    def vacia(self):
        return self.__cant == 0
    def insertar(self, numero):
        nodo = Nodo(numero)
        actual = self.__cabeza
        if(self.vacia()):
            self.__cabeza = nodo
            self.__cant += 1
        else:
            while actual.getSiguiente() is not None:
                actual = actual.getSiguiente()
            actual.setSiguiente(nodo)
            self.__cant += 1
        return numero
    def suprimir(self):
        result = None
        if(self.vacia()):
            print("La cola esta vacia.")
        else:
            result = self.__cabeza.getDato()
            self.__cabeza = self.__cabeza.getSiguiente()
            self.__cant -= 1
        return result
    def recorrer(self):
        actual = self.__cabeza

        while actual is not None:
            print(actual.getDato())
            actual = actual.getSiguiente()

        