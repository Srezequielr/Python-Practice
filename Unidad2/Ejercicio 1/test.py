from claseSube import Sube
from manejadorSube import ManejadorSube

def test():
    tarifa = 500
    manejadorUno = ManejadorSube()
    marca = int
    
    manejadorUno.agregarSube(input("Ingrese numero de sube 1: "));
    manejadorUno.agregarSube(input("Ingrese numero de sube 2: "));
    manejadorUno.agregarSube(input("Ingrese numero de sube 3: "));  
    

    numero = input("Ingrese numero de tarjeta: ")
    monto = int(input("Ingrese monto a cargar: ")) 
    marca = manejadorUno.cargarSaldo(numero, monto)
    if marca != -1:
        print(f"Carga exsitosa, saldo: {marca}")
    else:
        print("Error en la carga")
        
        
    numero = input("Ingrese numero de tarjeta: ")
    monto = int(input("Ingrese monto a cargar: "))
    marca = manejadorUno.cargarSaldo(numero, monto)
    if marca != -1:
        print(f"Carga exsitosa, saldo: {marca}")
    else:
        print("Error en la carga")
    
        
    numero = input("Ingrese numero de tarjeta: ")
    print(manejadorUno.verSaldo(numero))
    
    print(manejadorUno.pagarPasaje("1", tarifa))
    print(manejadorUno.pagarPasaje("3", tarifa))
    

    manejadorUno.verSubesNeg()
    
if __name__ == '__main__':
    test()