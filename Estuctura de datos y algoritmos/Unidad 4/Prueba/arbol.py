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
        if(nodo.getDato() == nuevaHoja.getDato()):
            print("Elemento ya existente")
        elif(nodo.getDato() > nuevaHoja.getDato()):
            print("Me desplace a la izquiera")
            if(nodo.getIzq() == None):
                nodo.setIzq(nuevaHoja)
                print("Inserte...")
            else:
                self.__insertar(nodo.getIzq(), dato)
        elif(nodo.getDato() < nuevaHoja.getDato()):
            print("Me desplace a la derecha")
            if(nodo.getDer() == None):
                nodo.setDer(nuevaHoja)
                print("Inserte...")
            else:
                self.__insertar(nodo.getDer(), dato)
    
    def getRaiz(self):
        return self.__raiz

    def posOrden(self):
        pass

    def preOrden(self):
        pass

    def inOrden (self,subarbol):
        if subarbol != None:
            self.inOrden(subarbol.getIzq())
            print(subarbol.getDato())
            self.inOrden(subarbol.getDer())

    def suprimir(sels):
        pass

    def vacio(self):
        return self.getRaiz() == None
    
    def esHoja(self, subArbol):
        return subArbol.getIzq() == None and subArbol.getDer() == None

    def buscar(self, subArbol, x):
        if(self.vacio()):
            print("El arbol esta vacio")
        else:
            if(subArbol == None):
                print("No se encuentro el elemento")
            elif(x == subArbol.getDato()):      
                print(f"Encontro el elemento: {subArbol.getDato()}")  
                return subArbol
            elif(x < subArbol.getDato()):
                print("Mi x es menor, me voy a la izquierda")
                return self.buscar(subArbol.getIzq(), x)
            else:
                print("Mi x es mayor, me voy a la derecha.")
                return self.buscar(subArbol.getDer(), x)
    
    def suprimir(self, elem):
        if(self.buscar(elem) == None):
            print("Elemento inexistente.")




    
            

