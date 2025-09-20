from nodo import Nodo
 
class Cola: 
    __cant: int
    __cabeza: object
    def __init__(self):
        self.__cabeza = None
        self.__cant = 0
    def vacia(self):
        return self.__cant == 0
    def insertar(self, tLlegada, cantPag):
        nuevoNodo = Nodo(tLlegada,cantPag)
        result = None
        if(self.vacia()):
            self.__cabeza = nuevoNodo
            self.__cant += 1
            result = tLlegada
        else:
            actual = self.__cabeza
            while actual.getSiguiente() is not None:
                actual =  actual.getSiguiente()
            actual.setSiguiente(nuevoNodo)
            self.__cant += 1
            result = tLlegada
        return result
    def suprimir(self):
        result = None
        if(self.vacia()):
            print("La lista esta vacia.")
        else:
            result = self.__cabeza
            self.__cabeza = self.__cabeza.getSiguiente()
            self.__cant -= 1
        return result
    def getCant(self):
        return self.__cant
    def recorrer(self):
        actual = self.__cabeza
        while actual is not None:
            print(f"Cantidad de paginas: {actual.getCanPag()} Tiempo de llegada: {actual.getTllegada()}" )
            actual = actual.getSiguiente()