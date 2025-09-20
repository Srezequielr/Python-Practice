from nodo import Nodo

class Arbol:
    __raiz: Nodo
    def __init__(self):
        self.__raiz = None
    def insertar(self, dato):
        if(self.__raiz == None):
            self.__raiz = Nodo(dato)
        else:
            self.__insertar(self.__raiz)

    def __insertar(self, dato, raiz):
        nuevaHoja = Nodo(dato)
        if(raiz == None):
            print("Inserte...")
            raiz = nuevaHoja
        elif(raiz.getDato() == nuevaHoja.getDato()):
            print("Elemento ya existente")
        elif(raiz.getDato() < nuevaHoja.getDato()):
            print("Me desplace a la izquiera")
            self.insertar(dato, raiz.getIzq())
        elif(raiz.getDato() > nuevaHoja.getDato()):
            print("Me desplace a la derecha")
            self.insertar(dato, raiz.getDer())
    def getRaiz(self):
        return self.__raiz







