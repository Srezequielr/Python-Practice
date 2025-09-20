from lista import Lista

def main():
    lista = Lista()

    lista.suprimir(2)
    lista.insertar(1, 9)   
    lista.insertar(1, 2)   
    lista.insertar(1, 5)   
    lista.insertar(1, 7)   
    lista.insertar(1, 6)  
    lista.insertar(1, 1)  
    
    
    lista.suprimir(5)
    lista.suprimir(1)
    lista.recorrer()                                                          



if __name__ == "__main__":
    main()