from nodo import Nodo

class Lista:
    __ult: int
    __cabeza: Nodo
    def __init__(self):
        self.__cabeza = None
        self.__ult = -1 
    def vacia(self):
        return self.__ult == - 1
    def insertar(self, pos, numero):
        result = None
        if(self.vacia()):
            print("Lista vacia, insertando al comienzo.")
            nuevoNodo = Nodo(numero)
            self.__ult += 1
            self.__cabeza = nuevoNodo
            result = numero
        elif(not pos - 1 > self.__ult):
            nuevoNodo = Nodo(numero)
            i = 0
            anterior = None
            actual = self.__cabeza
            while i < pos - 1:
                anterior = actual
                actual = actual.getSiguiente()
                i += 1
            self.__ult += 1
            if(anterior != None):
                anterior.setSiguiente(nuevoNodo) 
            else:
                self.__cabeza = nuevoNodo
            nuevoNodo.setSiguiente(actual)
            result = numero
        else:
            print("Posicion invalida.")
        return result
    
    def suprimir(self, pos):
        result = None
        if(self.vacia()):
            print("La lista esta vacia")
        elif(not pos - 1 > self.__ult):
            i = 0
            anterior = None
            actual = self.__cabeza
            while i < pos - 1:
                anterior = actual
                actual = actual.getSiguiente()
                i += 1
            self.__ult -=1
            result = actual.getDato()
            if (anterior != None):
                anterior.setSiguiente(actual.getSiguiente())
            else:
                self.__cabeza = actual.getSiguiente()
        else:
            print("posicion invalida")
        return result
    def primero(self):
        result = None
        if(self.vacia()):
            print("Lista vacia")
        else:
            result = self.__cabeza.getDato()
        return result
    def ultimo(self):
        result = None
        if(self.vacia()):
            print("Lista vacia.")
        else:
            actual = self.__cabeza
            while actual.getSiguiente() != None:
                actual = actual.getSiguiente()
            result = actual.getDato()
        return result
    def anterior(self, pos):
        result = None
        if(pos - 2 < 0 or pos - 2 > self.__ult):
            print("Posicion invalida.")
        else:
            i = 0
            anterior = None
            actual = self.__cabeza
            while i < pos - 1:
                anterior = actual
                actual = actual.getSiguiente()
                i += 1
            result = anterior.getDato()
        return result
    def siguiente(self, pos):
        result = None
        if(pos - 1 < 0 or pos - 2 > self.__ult):
            print("Posicion invalida.")
        else:
            i = 0
            actual = self.__cabeza
            while i < pos - 1:
                actual = actual.getSiguiente()
                i += 1
            result = actual.getSiguiente().getDato()
        return result 
    def buscar(self, elem):
        result = None
        i = 0
        encontrado = False
        actual = self.__cabeza
        while i < self.__ult and not encontrado:
            if(actual.getDato() == elem):
                encontrado = True
                result = i + 1
            actual = actual.getSiguiente()
            i += 1
        return result
    def recorrer(self):
        actual = self.__cabeza
        while actual != None:
            print(actual.getDato())
            actual = actual.getSiguiente()
    