from arbol import Arbol

def main():
    arbol = Arbol()

    arbol.insertar(85)
    arbol.insertar(30)
    arbol.insertar(40)
    arbol.insertar(5)
    arbol.insertar(34)
    arbol.insertar(12)
    
    xRaiz = arbol.getRaiz()

    arbol.inOrden(xRaiz)

    print(arbol.buscar(xRaiz, 5))

if __name__ == "__main__":
    main()