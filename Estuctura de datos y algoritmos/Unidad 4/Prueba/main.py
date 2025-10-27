from arbol import Arbol

def main():
    arbol = Arbol()
    cont = 1

    arbol.insertar(85)

    # ===== Elimina el primer nodo del arbol si es unico =====
    # if(arbol.getRaiz().grado() == 0):
    #     arbol.setRaiz(None)
    # ====================

    # ===== Insertar numeros =====
    arbol.insertar(30)
    arbol.insertar(40)
    arbol.insertar(5)
    arbol.insertar(34)
    arbol.insertar(12)
    arbol.insertar(100)
    arbol.insertar(120)
    arbol.insertar(90)
    # ====================
    
    # ===== Obtengo la raiz para las demas operaciones =====
    xRaiz = arbol.getRaiz()
    # ====================

    # =====  ===== 
    # arbol.posOrden(xRaiz)
    # ====================

    # =====  =====
    # arbol.inOrden(xRaiz)
    # ====================


    # arbol.suprimir(34, xRaiz, xRaiz, xRaiz)

    # ===== Devuelve el nodo mayor y menor, respectivamente =====
    # arbol.minimo(xRaiz)
    # arbol.maximo(xRaiz)
    # ====================

    # ===== Ver Sub arboles del lado izquierdo dado un nodo =====
    # arbol.verSubIzq(85)
    # ====================

    # ===== Mostrar nodos del mismo nivel de un nodo dado =====
    # arbol.mostrarXnivel(xRaiz ,arbol.buscarNivel(xRaiz, 5, cont), 1)
    # ====================
    
    # ===== Busca un nodo dada una clave =====
    # print(arbol.buscar(xRaiz, 5))
    # ====================

    arbol.hijo(30, 40)

    arbol.padre(30, 40)

if __name__ == "__main__":
    main()