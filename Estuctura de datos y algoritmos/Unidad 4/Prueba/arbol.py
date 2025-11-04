from nodo import Nodo

class Arbol:
    __raiz: Nodo
    def __init__(self):
        self.__raiz = None
    
    # ===== Obtener Raiz =====
    def getRaiz(self):
        return self.__raiz
    # ====================

    # ===== Setear Raiz =====
    def setRaiz(self, dato):
        self.__raiz = dato
    # ====================

    # ===== Ver si el arbol esta vacio =====
    def vacio(self):
        return self.getRaiz() == None
    # ====================

    # ===== Ver si el nodo es hoja TAD ESPEC=====
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
            if(nodo.getIzq() == None):
                nodo.setIzq(nuevaHoja)
            else:
                self.__insertar(nodo.getIzq(), dato)
        elif(nodo.getDato() < nuevaHoja.getDato()):
            if(nodo.getDer() == None):
                nodo.setDer(nuevaHoja)
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

    # ===== Mostrar nivel de un nodo TAD ESPEC=====
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
                cont += 1
                return self.buscarNivel(subArbol.getIzq(), x, cont)
            else:
                cont += 1
                return self.buscarNivel(subArbol.getDer(), x, cont)
    # ====================

    # ===== Buscar nodo, retorna el nodo TAD ESPEC===== 
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
                return self.buscar(subArbol.getIzq(), x)
            else:
                return self.buscar(subArbol.getDer(), x)
    # ====================

    # ===== Ve si un nodo X es hijo de un nodo Z TAD ESPEC =====
    def hijo(self, claveHijo, clavePadre):
        nodoPadre = self.buscar(self.getRaiz(), clavePadre)
        if(clavePadre < claveHijo):
            if(claveHijo == nodoPadre.getDer().getDato()):
                print(f"La clave {claveHijo} es hijo de clave {clavePadre}")
            else:
                print(f"La clave {claveHijo} NO es hijo de clave {clavePadre}")
        else:
            if(claveHijo == nodoPadre.getIzq().getDato()):
                print(f"La clave {claveHijo} es hijo de clave {clavePadre}")
            else:
                print(f"La clave {claveHijo} NO es hijo de clave {clavePadre}")
    # ====================

    # ===== Ve si un nodo X es padre de un nodo Z TAD ESPEC =====
    def padre(self, clavePadre, claveHijo):
        nodoPadre = self.buscar(self.getRaiz(), clavePadre)
        if(clavePadre < claveHijo):
            if(claveHijo == nodoPadre.getDer().getDato()):
                print(f"La clave {clavePadre} es padre de clave {claveHijo}")
            else:
                print(f"La clave {clavePadre} NO es hijo de clave {claveHijo}")
        else:
            if(claveHijo == nodoPadre.getIzq().getDato()):
                print(f"La clave {clavePadre} es hijo de clave {claveHijo}")
            else:
                print(f"La clave {clavePadre} NO es hijo de clave {claveHijo}")
    # ====================

    # ===== Contar 1 Descendiente recursivo ===== 
    def unDescendiente_iterativo(self, raiz):

        cont = 0
        stack = []      # La pila para simular la recursión
        actual = raiz   # Empezamos en la raíz

        # El bucle debe continuar mientras 'actual' no sea None (aún bajando)
        # O mientras la pila no esté vacía (aún tenemos nodos por visitar)
        while actual is not None or len(stack) > 0:

            # --- 1. Parte IZQUIERDA ---
            # Navega lo más a la izquierda posible
            # Apilamos los nodos a medida que bajamos para "recordarlos"
            while actual is not None:
                stack.append(actual)
                actual = actual.getIzq()

            # --- 2. Parte RAÍZ ---
            # Si llegamos aquí, 'actual' es None (tocamos fondo a la izquierda).
            # El último nodo válido que vimos está en el tope de la pila.
            # Lo sacamos (pop) para "visitarlo".
            actual = stack.pop()

            if(actual.grado() == 1):
                cont += 1
            
            # (Aquí podrías hacer print(actual.valor) en lugar de añadir a la lista)

            # --- 3. Parte DERECHA ---
            # Ya visitamos la izquierda y la raíz, ahora vamos a la derecha.
            # El bucle principal se encargará de, en la siguiente iteración,
            # encontrar el nodo más a la izquierda de esta nueva rama derecha.
            actual = actual.getDer()

        return cont
    # ====================

    # ===== Contar 1 Descendiente =====
    def unDescendiente(self, subArbol, cont):
        if(subArbol != None):
            if (subArbol.grado() == 1):
                cont += 1
            # 2. Recorrer la izquierda
            # Pasamos el contador actual. La función nos devolverá
            # el contador + todo lo que encontró en la rama izquierda.
            # ACTUALIZAMOS nuestro contador con ese nuevo total.
            cont = self.unDescendiente(subArbol.getIzq(), cont)

            # 3. Recorrer la derecha
            # Pasamos el contador (que YA incluye lo de la izquierda)
            # a la rama derecha. De nuevo, ACTUALIZAMOS el contador
            # con el total que regrese.
            cont = self.unDescendiente(subArbol.getDer(), cont)

            # 4. Devolver el total acumulado de esta rama
            return cont
        else:
            return cont
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