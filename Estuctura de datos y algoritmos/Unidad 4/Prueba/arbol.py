from nodo import Nodo

class Arbol:
    __raiz: Nodo
    def __init__(self):
        self.__raiz = None
    
    # ===== Obtener Raiz =====
    def getRaiz(self):
        return self.__raiz
    # ====================

    # ===== Setear Raiz
    def setRaiz(self, dato):
        self.__raiz = dato
    # ====================

    # ===== Ver si el arbol esta vacio =====
    def vacio(self):
        return self.getRaiz() == None
    # ====================

    # ===== Ver si el nodo es hoja =====
    def esHoja(self, subArbol):
        return subArbol.grado() == 0
    # ====================

    # ===== Insertar Raiz =====
    def insertar(self, dato):
        if(self.__raiz == None):
            self.setRaiz(Nodo(dato))
        else:
            self.__insertar(self.__raiz, dato)
            
    # ===== Insertar Recursivo =====
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
    # ====================
    
    # ===== Recorridos =====
        # ===== Pos Orden =====
    def posOrden(self, subArbol):        
        if subArbol != None:
            self.posOrden(subArbol.getIzq())
            self.posOrden(subArbol.getDer())
            print(f"{subArbol.getDato()}")

        # ===== Pre Orden =====
    def preOrden(self,subArbol):
         if subArbol != None:
            print(f"{subArbol.getDato()}")
            self.posOrden(subArbol.getIzq())
            self.posOrden(subArbol.getDer())

        # ===== In Orden =====
    def inOrden (self,subarbol):
        if (subarbol != None):
            self.inOrden(subarbol.getIzq())
            print(f"{subarbol.getDato()}")
            self.inOrden(subarbol.getDer())
    # ====================

    # ===== Ver arbol de un Sub Arbol Izquierdo =====
    def verSubIzq(self, clave):
        subArbol = self.buscar(self.getRaiz(), clave)
        self.preOrden(subArbol.getIzq())
    # ====================

    # ===== Nodo Minimo =====
    def minimo (self,subarbol):
        if (subarbol.getIzq() != None):
            self.minimo(subarbol.getIzq())
        else:
            print(f"{subarbol.getDato()}")
    # ====================

    # ===== Nodo Maximo =====
    def maximo (self,subarbol):
        if (subarbol.getDer() != None):
            self.maximo(subarbol.getDer())
        else:
            print(f"{subarbol.getDato()}")
    # ====================


    # ===== Mostrar Nodos dado un nivel =====
    def mostrarXnivel(self, subArbol, nivel, cont):
        if(subArbol != None):
            if(cont == nivel):
                print(subArbol.getDato())
            self.mostrarXnivel(subArbol.getIzq(), nivel, cont + 1)
            self.mostrarXnivel(subArbol.getDer(), nivel, cont + 1)
    # ====================

    # ===== Mostrar nivel de un nodo =====
    def buscarNivel(self, subArbol, x, cont):
        if(self.vacio()):
            print("El arbol esta vacio")
        else:
            if(subArbol == None):
                print("No se encuentro el elemento")
            elif(x == subArbol.getDato()):      
                print(f"Encontro el elemento: {subArbol.getDato()}, en el nivel {cont}")  
                return cont
            elif(x < subArbol.getDato()):
                print("Mi x es menor, me voy a la izquierda")
                cont += 1
                return self.buscarNivel(subArbol.getIzq(), x, cont)
            else:
                print("Mi x es mayor, me voy a la derecha.")
                cont += 1
                return self.buscarNivel(subArbol.getDer(), x, cont)
    # ====================

    # ===== Buscar nodo, retorna el nodo ===== 
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
    # ====================
    
    def suprimir(self, dato, aux, ant,ult):
            if self.vacio():
                print("error el arbol esta vacio")
            else:
                if((aux.getDer()!=None or aux.getIzq()!=None) and dato!=aux.getDato()):
                    if (dato < aux.getDato()) and (aux.getIzq() != None):
                        print("Izquierdo", aux.getDato())
                        ant=aux
                        aux=aux.getIzq()
                        ult=aux.getDer()
                        self.suprimir(dato, aux, ant, ult)
                    else:
                        print("Derecho", aux.getDato())
                        if(aux.getDer() != None):
                            ant=aux
                            aux=aux.getDer()
                            ult=aux.getDer()
                            self.suprimir(dato, aux, ant, ult)
                if(aux.getDato()==dato):
                    if ult.getIzq() != None:
                        if ult.getIzq().getIzq() == None:
                            aux2=ult.getIzq()
                            ult.setIzq(ult.getIzq().getDer())
                            ult=aux2
                        else:
                            ult=ult.getIzq()
                            self.suprimir(dato,aux,ant,ult)
                    else:
                        ant.setIzq(ult)
                        ult.setIzq(aux.getIzq())
                        ult.setDer(aux.getDer())