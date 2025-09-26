from lista import Lista

def main():
    lista = Lista()

    lista.insertar(1, 5)
    lista.insertar(1, 3)
    lista.insertar(1, 78)
    lista.insertar(1, 9)
    lista.insertar(1, 33)

    lista.suprimir(3)

    print("Primer elemento: ", lista.primero())
    print("Ultimo elemento: ", lista.ultimo())
    print("Elemento siguiente: ", lista.siguiente(2))
    print("Elememento anterior: ", lista.anterior(5))
    print("Resultado de busqueda: ", lista.buscar(9))
    lista.recorrer()





if __name__ == "__main__":
    main()