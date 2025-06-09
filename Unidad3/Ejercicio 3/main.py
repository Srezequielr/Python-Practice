from manejadorEmpleado import ManejadorEmpleado
from manejadorMatricula import ManejadorMatricula
from manejadorProgCapacitacion import ManejadorProgCapacitacion

def menu():
    opcion = int(input("""
[1]. Buscar duracion de los programas del empleado
[2]. Ver empleados matriculados por nombre de programa
[3]. Ver empleados sin matriculas
Ingresar opcion: """))
    return opcion

def main():
    manEmp = ManejadorEmpleado()
    manProg = ManejadorProgCapacitacion()
    manMat = ManejadorMatricula(manEmp, manProg)
    
    manEmp.cargarCSV()
    manProg.cargaCSV()
    manMat.cargaCSV()
    
    
    opcion = menu()
    while opcion != 0:
        if opcion == 1:
            idEmpleado = int(input("Ingresar ID del empleado"))
            manMat.verProgramasPorEmpleado(idEmpleado)
        elif opcion == 2:
            nomProg = input("Ingresar nombre del programa: ")
            manMat.verMatriculados(nomProg)
        elif opcion == 3:
            manMat.verEmpleadosSinMatricula()
        elif opcion == 0:
            print("Saliendo...")
        opcion = menu()
            
            
if __name__ == "__main__":
    main()
    