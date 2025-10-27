from nodo import Nodo

class Arbol:
    __raiz: Nodo
    def __init__(self):
        self.__raiz = None
    def getRaiz(self):
        return self.__raiz
    
    # Solo metodos vistos en teoria

    # ===== Insertar =====
    def insertar(self, clave):
        if(self.__raiz == None):
            self.__raiz = Nodo(clave)
        else:
            self.__insertar(self.__raiz, clave)
    
    def __insertar(self, subArbol, clave):
        if(subArbol.getDato() == clave):
            print("Clave ya existente")
        if(clave < subArbol.getDato()):
            if(subArbol.getIzq() == None):
                subArbol.setIzq(Nodo(clave))
            else:
                return self.__insertar(subArbol.getIzq(), clave)
        else:
            if(subArbol.getDer() == None):
                subArbol.setDer(Nodo(clave))
            else:
                return self.__insertar(subArbol.getDer(), clave)
    # ====================

    # ===== Suprimir (Para despues jeje) =====
    def suprimir(self, clave):
        pass
    # ====================

    # ===== Buscar un nodo ===== 
    def buscar(self, subArbol, clave):
        if(subArbol == None):
            print("No se encontro el elemento.")
