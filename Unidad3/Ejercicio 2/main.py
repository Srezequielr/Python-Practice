from manejadorBiblioteca import ManejadorBiblioteca

def menu():
    opcion = int(input("""
Menu:
[1]. Agregar libro
[2]. Eliminar libro
[3]. Buscar libro
[4]. Mostrar libros
[0]. Salir
Ingrese opcion: """))
    return opcion


def main():
    manBiblioteca = ManejadorBiblioteca()
    
    manBiblioteca.cargarCSV()
    
    opcion = menu()
    while opcion != 0:
        if opcion == 1:
            manBiblioteca.agregarLibro()
        elif opcion == 2:
            manBiblioteca.eliminarLibro()
        elif opcion == 3:
            manBiblioteca.verLibrosEnBibliotecas()
        elif opcion == 4:
            manBiblioteca.verLibrosDisponibles()
        elif opcion == 0:
            print("Chau ;)")
        else:
            print("Opcion invalida") 
        opcion = menu()
            
            
if __name__ == "__main__":
    main()