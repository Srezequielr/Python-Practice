from claseSube import Sube
from manejadorSube import ManejadorSube

def test():
    tarifa = 500
    manejadorUno = ManejadorSube()
    
    print("Ingrese numero de sube 1")
    manejadorUno.agregarSube(input());
    print("Ingrese numero de sube 2")
    manejadorUno.agregarSube(input());
    print("Ingrese numero de sube 3")
    manejadorUno.agregarSube(input());  
    print("Ingrese monto a cargar")
    monto = int(input()) 
    print("Ingrese numero de tarjeta")    
    numero = input()
    
    manejadorUno.cargarSaldo(monto, numero)
    print("Ingrese monto a cargar")
    monto = int(input())
    print("Ingrese numero de tarjeta")    
    numero = input()
    manejadorUno.cargarSaldo(monto, numero)
    
    print(manejadorUno.pagarPasaje(tarifa, "1"))
    print(manejadorUno.pagarPasaje(tarifa, "2"))
    
    

    
    manejadorUno.verSaldoNeg()
if __name__ == '__main__':
    test()