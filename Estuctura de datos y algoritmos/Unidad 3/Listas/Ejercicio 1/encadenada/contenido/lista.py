from nodo import Nodo

class Lista:
    __cabeza: object
    __ult: int
    def __init__(self):
        self.__cabeza = None
        self.__ult = -1
    def vacia(self):
        return self.__ult == -1
    def insertar(self, numero):
        result = None
        if(self.vacia()):
            nuevoNodo = Nodo(numero)
            print("Lista vacia, insertanto al comienzo.")
            self.__ult += 1
            self.__cabeza = nuevoNodo
            result = numero
        else:
            nuevoNodo = Nodo(numero)
            anterior = None
            actual = self.__cabeza
            while actual != None and numero > actual.getDato():
                anterior = actual
                actual = actual.getSiguiente() 
            self.__ult += 1
            result = numero
            if(anterior == None):
                nuevoNodo.setSiguiente(self.__cabeza)
                self.__cabeza = nuevoNodo
            else:
                anterior.setSiguiente(nuevoNodo)
                nuevoNodo.setSiguiente(actual)  
        return result
    def recorrer(self):
        if(self.vacia()):
            print("La lista esta vacia.")
        else:
            actual = self.__cabeza
            while actual != None:
                print(actual.getDato())
                actual = actual.getSiguiente()