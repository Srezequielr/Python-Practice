from nodo import Nodo

class Lista:
    __cabeza: object
    def __init__(self):
        self.__cabeza = None
        
    def insertar(self, valor):
        nuevoNodo = Nodo(valor)
        nuevoNodo.setSig(self.__cabeza)
        self.__cabeza = nuevoNodo

    def vacia(self):
        return self.__cabeza == None

    def recorrer(self):
        if(self.vacia()):
            print("La lista esta vacia.")
        else:
            actual = self.__cabeza
            while actual != None:
                print(actual.getDato())
                actual = actual.getSig()

    def buscar(self, clave):
        encontrado = False
        actual = self.__cabeza

        while not encontrado and actual != None:
            if(actual.getDato() == clave):
                encontrado = True
            actual = actual.getSig()
        
        return encontrado
        

