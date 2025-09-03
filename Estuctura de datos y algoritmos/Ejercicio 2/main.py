from pila import PILA

def main():
    numero = int(input("Ingrese numero a pasar a binario: "))
    pila = PILA()  
    while(numero >= 1):
        resto = numero % 2
        numero = int( numero / 2)
        if(resto != 0):
            resto = 1
        pila.insertar(resto)        
    pila.recorrer()    
    
if __name__ == "__main__":
    main()