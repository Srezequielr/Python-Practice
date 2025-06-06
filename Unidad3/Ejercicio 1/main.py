from manejadorHotel import ManejadorHotel

def menu():
    try:
        opcion = int(input("""Ingrese opcion:
1. Agregar habitacion
2. Revervar habitacion
3. Liberar habitacion
4. Mostrar habitaciones de un tipo
5. Mostrar habitaciones libres por piso
6. Mostrar habitaciones
Opcion: """))
        return opcion
    except ValueError:
        print("No ingreso un numero valido")
    


def main():
    manHotel = ManejadorHotel()
    manHotel.cargarDatos()
    

    opcion = menu()
    
    while opcion != 0:
        if opcion == 1:
            manHotel.agregarHabitacion()
        elif opcion == 2:
            manHotel.reservarHabitacion()
        elif opcion == 3:
            manHotel.liberarHabitacion()
        elif opcion == 4:
            manHotel.mostrarHabXTipo()
        elif opcion == 5:
            manHotel.mostrarHabLibres()
        elif opcion == 6:
            pass
        else:
            print("Opcion invalida")
        opcion = menu()
        
if __name__ == "__main__":
    main()
    