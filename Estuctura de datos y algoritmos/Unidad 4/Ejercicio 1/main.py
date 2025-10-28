from arbol import Arbol

def main():
    arbol = Arbol()
    nivel = 1




    # ===== Insertar numeros =====
    arbol.insertar(85)
    arbol.insertar(30)
    arbol.insertar(40)
    arbol.insertar(5)
    arbol.insertar(34)
    arbol.insertar(12)
    arbol.insertar(100)
    arbol.insertar(120)
    arbol.insertar(90)
    arbol.insertar(20)
    # ====================
    xRaiz = arbol.getRaiz()
    
    # ===== Buscar nodo =====
    arbol.buscar(xRaiz, 40)
    # ====================

    # ===== Ver nivel de un nodo =====
    print(f"Nivel del nodo: {arbol.nivel(xRaiz, nivel, 40)}")
    # ====================

    # ===== Ver si el nodo es hoja o no =====
    arbol.hoja(85)
    arbol.hoja(12)
    # ====================

    # ===== Padre e hijo =====
    arbol.hijo(30, 40)
    arbol.padre(30, 40)
    # ====================

    # ===== Calcular altura del arbol =====
    print(f"Nivel de arbol {arbol.altura(xRaiz)}") 
    # ====================

if __name__ == "__main__":
    main()