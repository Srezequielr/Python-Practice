from hashEncadenada import HashEncadenado
import random

def main():
    hashingEnc = HashEncadenado()

    for _ in range(1,100):
        hashingEnc.insertar(random.randint(4600,4699))

    hashingEnc.recorrerHash()

    busqueda = int(input("Ingrese valor a buscar: "))
    hashingEnc.buscar(busqueda)


if __name__ == "__main__":
    main()