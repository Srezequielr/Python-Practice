from lista import Lista

def main():
    lista = Lista()

    lista.suprimir(2)

    lista.insertar(23)
    lista.insertar(5)
    lista.insertar(10)
    lista.insertar(22)
    lista.insertar(15)

    

    lista.recorrer()


    print(lista.siguiente(4))
    print(lista.anterior(6))
    print("Primer elemento: ", lista.primer())
    print("Ultimo elemento: ", lista.ultimo())

    print("El elemento esta en la posicion: ",  lista.buscar(15) + 1)

if __name__ == "__main__":
    main()