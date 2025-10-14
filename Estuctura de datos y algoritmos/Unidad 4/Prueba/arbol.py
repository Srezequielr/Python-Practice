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
            if(nodo.getIzq() == None):
                nodo.setIzq(nuevaHoja)
                print("Inserte...")
            else:
                self.__insertar(nodo.getIzq(), dato)
        elif(nodo.getDato() > nuevaHoja.getDato()):
            print("Me desplace a la derecha")
            if(nodo.getDer() == None):
                nodo.setDer(nuevaHoja)
                print("Inserte...")
            else:
                self.__insertar(nodo.getDer(), dato)
    
    def getRaiz(self):
        return self.__raiz


    def inorden (self,subarbol):
        if subarbol != None:
            self.inorden(subarbol.getIzq())
            print(subarbol.getDato())
            self.inorden(subarbol.getDer())





if __name__ == "__main__":
    arbol = Arbol()

    arbol.insertar(70)
    arbol.insertar(30)
    arbol.insertar(80)
    arbol.insertar(50)
    arbol.insertar(75)
    arbol.insertar(20)
    xRaiz = arbol.getRaiz()
    arbol.inorden(xRaiz)


    
            

