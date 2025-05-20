

def menu():
    op = int(input("""
                   Ingerese una opcion:
                   1. Mostrar accidentes por departamento
                   2. Mostrar departamento con mas accidentes en el mes
                   3. Mostrar accidentes totales de un departamento
                   4. Mostrar datos"""))
    return op
    

if __name__ == '__main__':
    opcion = menu()