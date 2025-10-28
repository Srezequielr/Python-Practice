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
        if(subArbol.getDato() == clave):
            print("Se encontro el nodo.")
            return subArbol
        else:
            if(subArbol.getDato() < clave):
                return self.buscar(subArbol.getDer(), clave)
            else:
                return self.buscar(subArbol.getIzq(), clave)
    # ====================

    # ===== Dar el nivel de un nodo =====
    def nivel(self, subArbol, nivel, clave):
        if(subArbol == None):
            print("No se encontro el nodo")
        if(subArbol.getDato() == clave):
            return nivel
        else:
            if(subArbol.getDato() < clave):
                return self.nivel(subArbol.getDer(), nivel + 1, clave)
            else:
                return self.nivel(subArbol.getIzq(), nivel + 1, clave)
    # ====================

    # ===== Ver si un nodo es hoja =====
    def hoja(self, clave):
        result = None 
        nodo = self.buscar(self.getRaiz(), clave)
        if(nodo.grado() == 0):
            print("El nodo es hoja")
            result = 1
        else:
            print("El nodo no es hoja")
        return result
    # ====================

    # ===== Ver si un nodo X es hijo de un nodo Z =====
    def hijo(self, claveHijo, clavePadre):
        result = None
        nodoPadre = self.buscar(self.getRaiz(), clavePadre)
        if(nodoPadre == None):
            print("Error: no se encontro el nodo padre")
        else:
            if(clavePadre < claveHijo):
                if(nodoPadre.getDer().getDato() == claveHijo):
                    print(f"El nodo clave {claveHijo} es hijo de nodo clave {clavePadre}.")
                    result = 1
                else:
                    print(f"El nodo clave {claveHijo} NO es hijo de nodo clave {clavePadre}.")
            else:
                if(nodoPadre.getIzq().getDato() == claveHijo):
                    print(f"El nodo clave {claveHijo} es hijo de nodo clave {clavePadre}")
                    result = 1
                else:
                    print(f"El nodo clave {claveHijo} NO es hijo de nodo clave {clavePadre}.")
        return result
    # ====================

    # ===== Ver si un nodo X es padre de un nodo Z =====
    def padre(self, clavePadre, claveHijo):
        result = None
        nodoPadre = self.buscar(self.getRaiz(), clavePadre)
        if(nodoPadre == None):
            print("Error: no se encontro el nodo padre")
        else:
            if(clavePadre < claveHijo):
                if(nodoPadre.getDer().getDato() == claveHijo):
                    print(f"El nodo clave {clavePadre} es padre de nodo clave {claveHijo}.")
                    result = 1
                else:
                    print(f"El nodo clave {clavePadre} NO es padre de nodo clave {claveHijo}.")
            else:
                if(nodoPadre.getIzq().getDato() == claveHijo):
                    print(f"El nodo clave {clavePadre} es padre de nodo clave {claveHijo}")
                    result = 1
                else:
                    print(f"El nodo clave {clavePadre} NO es padre de nodo clave {claveHijo}.")
        return result
    # ====================

    # ===== Ver el camino de un nodo X hacia un nodo Z =====
    def camino(self, claveX, claveZ):
        pass
        # Preguntar en consulta
    # ====================

    # ===== Calcula la altura del arbol =====
    def altura(self, subArbol):
        if(subArbol == None):
            return 0
        
        alturaDerecha = self.altura(subArbol.getDer())
        alturaIzquierda = self.altura(subArbol.getIzq())

        if(alturaDerecha < alturaIzquierda):
            return 1 + alturaIzquierda
        else:
            return 1 + alturaDerecha

    # ====================

    # ===== PreOrden =====
    def preOrden(self, subArbol):   # Raiz -> izquierda -> derecha
        if(subArbol != None):
            print(subArbol.getDato())
            self.preOrden(subArbol.getIzq())
            self.preOrden(subArbol.getDer())
    # ====================

    # ===== PosOrden =====
    def posOrden(self, subArbol):   # izquierda -> derecha -> Raiz
        if(subArbol != None):
            self.preOrden(subArbol.getIzq())
            self.preOrden(subArbol.getDer())
            print(subArbol.getDato())
    # ====================

    # ===== InOrden =====
    def inOrden(self, subArbol):    # izquierda -> Raiz -> derecha 
        if(subArbol != None):
            self.preOrden(subArbol.getIzq())
            print(subArbol.getDato())
            self.preOrden(subArbol.getDer())
    # ====================
        