from manejadorColectivo import ManejadorColectivo
from manejadorTramo import manejadorTramo

def menu():
    opcion = int(input("""Ingresar opcion:
                   1- Obtener lista de tramos por DNI 
                   2- Mostrar kilometros recorridos y gasto por colectivo
                   3- Mostrar tramos con X kilometros
                   0- Finalizar \n"""))
    return opcion

if __name__ == '__main__':
    option = None
    manCol = ManejadorColectivo()
    manCol.cargarDatos()
    manTram = manejadorTramo(manCol)
    manTram.cargarDatos()

    while option != 0:
        option = menu()
        if option == 1:
            manTram.listaTramos()
        elif option == 2:
            manTram.listarColectivos()
        elif option == 3:
            manTram.mostrarTramosMayores()
        elif option == 0:
            print("Fin del programa")