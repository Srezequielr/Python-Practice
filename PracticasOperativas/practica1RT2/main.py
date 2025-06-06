##Julian riera


from manejadorEquipo import ManejadorEquipo
from manejadorResultado import manejadorResultado

def menu():
    opcion = input("""
    1- Mostrar equipos por fecha
    2- Ver resultados de local de equipo
    3- Mostrar tabla de posiciones
    0- Salir
    Ingrese una opcion: """)
    return opcion

def main():
    manEquipo = ManejadorEquipo()
    manResultado = manejadorResultado(manEquipo)
    
    manEquipo.cargarDatosEquipos()
    manResultado.cargarDatosResultados()
    
    opcion = menu()
    while opcion != "0":
        if opcion == "1":
            manResultado.verResultadosFecha()
        elif opcion == "2":
            pass
            manResultado.verResultadosLocalEquipo()
        elif opcion == "3":
            manResultado.cargarTablaPosiciones()
            manEquipo.ordenar()
            manEquipo.mostrarTablaPosiciones()
        else:
            print("Opcion no valida")
        opcion = menu()
    
    
    
    
if __name__ == "__main__":
    main()
