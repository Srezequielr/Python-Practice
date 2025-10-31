from hashAbierta import HashAbierto
import random

def main():
    hashAbierto = HashAbierto()
    for _ in range(1,100):
        hashAbierto.insertar(random.randint(4600,4699))

    hashAbierto.recorrer()

    busqueda = int(input("Ingrese elemento a buscar: "))
    hashAbierto.buscar(busqueda)



if __name__ == "__main__":
    main()