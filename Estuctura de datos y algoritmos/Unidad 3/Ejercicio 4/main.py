from tablero import Tablero

def main():
    print("Bienvenido al Juego!")
    tab = Tablero()
    tab.iniciarJuego()

    fin = False

    while not fin:
        tab.mover()
        tab.mostrarPilas()
        if(tab.gano()):
            fin = True
            print("Felicidades, ganaste!")

    print(f"Lo completaste en {tab.getMovimientos()} movimientos")

        



if __name__ == "__main__":
    main()