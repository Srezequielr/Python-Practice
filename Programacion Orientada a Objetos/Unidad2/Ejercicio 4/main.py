from manejadorFacultad import ManejadorFacultad
from manejadorCarrera import ManejadorCarrera

def menu():
    op = int(input("""Elija una opcion:
    1. Mostrar nombre de la facultad de una carrera
    2. Contar cantidad de carreras por facultad
    0. Salir
    Opcion:  """))

    return op

def main():
    manFac = ManejadorFacultad()
    manFac.cargarDatos()
    manCarrera = ManejadorCarrera(manFac)
    manCarrera.cargarDatos()
    op = menu()
    while (op != 0):
        if (op == 1):
            manCarrera.mostrarFacultad()
        elif (op == 2):
            manCarrera.contarCarreras()
        else:
            print("Opcion incorrecta")
        op = menu()    
if __name__ == "__main__":
    main()