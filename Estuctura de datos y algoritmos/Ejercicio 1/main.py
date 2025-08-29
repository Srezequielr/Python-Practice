from Pila import PILA

def main():
    pila = PILA()
    
    pila.suprimir()
    pila.insertar(4)
    pila.insertar(2)
    pila.insertar(5)
    pila.insertar(1)
    pila.insertar(30)
    pila.insertar(9)
    
    pila.suprimir()
    pila.suprimir()
    pila.suprimir()
    
    pila.recorrer()
    
if __name__ == "__main__":
    main()