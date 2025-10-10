from nodo import Nodo

class Arbol:
    __raiz: Nodo
    def __init__(self):
        self.__raiz = None
    def insertar(self, dato):
        if(self.__raiz == None):
            self.__raiz = Nodo(dato)
        else:
            self.__insertar(self.__raiz, dato)

    def __insertar(self, nodo, dato):
        nuevaHoja = Nodo(dato)
        if(nodo == None):
            print("Inserte...")
            nodo = nuevaHoja
        elif(nodo.getDato() == nuevaHoja.getDato()):
            print("Elemento ya existente")
        elif(nodo.getDato() < nuevaHoja.getDato()):
            print("Me desplace a la izquiera")
            self.__insertar(nodo.getIzq(), dato)
        elif(nodo.getDato() > nuevaHoja.getDato()):
            print("Me desplace a la derecha")
            self.__insertar(nodo.getDer(), dato)
    def getRaiz(self):
        return self.__raiz







