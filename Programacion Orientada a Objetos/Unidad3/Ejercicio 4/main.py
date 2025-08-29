from manPlanes import ManejadorPlanes

def menu():
    opcion = int(input("""
    Menu.
    1. Ver tipo de plan por codigo.
    2. Ver planes por covertura geografica.
    3. Ver planes con X o mas canales internacionales.
    4. Listar planes.
    0. Salir.
    Opcion: """))
    return opcion
    
def main():
    
    manPlanes = ManejadorPlanes()
    manPlanes.cargaCSV()
    
    opcion = menu()
    
    while(opcion != 0):
        if(opcion == 1):
            manPlanes.verTipoPlan()
        elif(opcion == 2):
            manPlanes.verPlanesXcobertura()
        elif(opcion == 3):
            manPlanes.verPlanesInt() 
        elif(opcion == 4):
            manPlanes.listarPlanes()
        elif(opcion == 0):
            print("Saliendo...")
        else:
            print("Opcion incorrecta.")
        opcion = menu()
        
        
if __name__ == "__main__":
    main()