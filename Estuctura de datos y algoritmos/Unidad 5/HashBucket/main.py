from tablaHash import HashBucket
import random

def main():
    bucket = HashBucket(100, 5)

    bucket.mostrarValores()

    for _ in range(1,100):
        bucket.insertar(random.randint(4600,4699))

    bucket.recorrerHash()

    busqueda = int(input("Ingrese numero a buscar: "))
    bucket.buscar(busqueda)


if __name__ == "__main__":
    main()