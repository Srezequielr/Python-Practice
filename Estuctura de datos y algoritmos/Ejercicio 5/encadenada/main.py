from cola import Cola

def main(): 
    cola = Cola()
    
    cola.suprimir()
    cola.insertar(6)
    cola.insertar(54)
    cola.insertar(4)
    cola.insertar(6)
    cola.insertar(23)
    cola.insertar(87)
    cola.suprimir()
    cola.suprimir()

    cola.recorrer()
    
    
if __name__ == "__main__":
    main()