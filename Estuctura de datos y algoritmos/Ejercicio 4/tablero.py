from pila import PILA

class Tablero:
    __tablero: list
    __movimientos: int
    def __init__(self):
        self.__tablero = []
        self.__tablero.append(PILA())  
        self.__tablero.append(PILA())  
        self.__tablero.append(PILA())  
        self.__movimientos = 0
    def iniciarJuego(self):
        self.__tablero[0].insertar(1)
        self.__tablero[0].insertar(2)
        self.__tablero[0].insertar(3)
        self.__tablero[0].insertar(4)
        self.__tablero[0].insertar(5)

    def mover(self):
        inicio = int(input("Ingrese numero de pila de origen: ")) 
        ficha = int
        if(self.__tablero[inicio - 1].vacia()):
            ficha = self.__tablero[inicio - 1].getPrimero()
            
        else:
            fin = int(input("Ingrese pila de destino: "))
            if(self.__tablero[fin - 1].vacia()):
                self.__tablero[fin -1].insertar(self.__tablero[inicio -1].suprimir())
                self.__movimientos += 1
            else:

                if(ficha > self.__tablero[fin - 1].getPrimero()):
                    print("Movimiento no permitido.")
                else:
                    self.__tablero[fin -1].insertar(self.__tablero[inicio -1].suprimir())
                    self.__movimientos += 1
    
    def gano(self):
        return self.__tablero[2].llena()  
    
    def getMovimientos(self):
        return self.__movimientos
    
    def mostrarPilas(self):
        for pila in self.__tablero:
            pila.mostrarPila()
        




