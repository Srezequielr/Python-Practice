from grafo import Grafo

def main():
    manGrafo = Grafo(5)

    manGrafo.crearArista(1, 4)
    manGrafo.crearArista(1, 2)
    manGrafo.crearArista(2, 3)
    manGrafo.crearArista(2, 5)
    manGrafo.crearArista(3, 2)
    manGrafo.crearArista(3, 4)

    # ===== Verifico entrada y salida de un nodo =====
    print( "Grado de entrada: ", manGrafo.gradoEntrada(4)) 
    print( "Grado de salida: ", manGrafo.gradoSalida(4)) 
    # ====================

    # ===== Verifico el sumidero de un nodo =====
    print("Este nodo es sumidero? ", manGrafo.nodoS(4))
    print("Este nodo es sumidero? ", manGrafo.nodoS(1))
    # ====================

    # ===== Verifico la fuente de un nodo =====
    print("Este nodo es fuente? ", manGrafo.nodoF(4))
    print("Este nodo es fuente? ", manGrafo.nodoF(1))
    # ====================


    manGrafo.recorrerMatAdy()



if __name__ == "__main__":
    main()