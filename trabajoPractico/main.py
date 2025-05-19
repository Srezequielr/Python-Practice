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
    op = menu()
    
    manCol = ManejadorColectivo()
    manCol.cargarDatos()
    manTram = manejadorTramo(manCol)
    manTram.cargarDatos()