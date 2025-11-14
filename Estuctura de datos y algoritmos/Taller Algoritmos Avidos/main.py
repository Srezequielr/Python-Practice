from cola import Cola

def main():
    listaTrabajos = [] # Candidatos

    # Cargamos la lista de trabajos
    i = 0
    durTrabajo = 1
    while durTrabajo != 0:
        durTrabajo = int(input(f"Ingrese duracion de trabajo {i + 1} \n 0 para cancelar: "))
        if durTrabajo != 0:
            listaTrabajos.append(durTrabajo)
    # ====================

    TiempoTotal = 0
    for trabajo in listaTrabajos:
        TiempoTotal += trabajo

    # Inicializamos la cola con el tamaño de la lista
    numTrabajos = len(listaTrabajos)
    colaOrdenada = Cola(numTrabajos) # Subconjunto Solucion 
    # ====================
    
    # Funcion de seleccion
    while len(listaTrabajos) != 0:
        j = 0
        menor = listaTrabajos[j]
        while j < len(listaTrabajos):
            if(listaTrabajos[j] < menor):
                menor = listaTrabajos[j]
            j += 1
        colaOrdenada.insertar(menor)
        listaTrabajos.remove(menor)
    # ====================

    input("Presione enter para iniciar la Sumulacion.")
    print("\n Iniciando Simulación de la Cola ---")

    Ttotal = 0
    acumulado = 0
    NCliente = 1
    TEspera = []
    print(f"Orden optimo de reparacion: {colaOrdenada}")
    
    while not colaOrdenada.vacia():
        
        DurTarea = colaOrdenada.suprimir() 
        TEspera.append(acumulado)
        print(f"  Cliente {NCliente} (tarea de {DurTarea} min): Espera = {acumulado} min")
        
        # El tiempo acumulado es el tiempo de espera para terminar la tarea
        acumulado += DurTarea
        
        # Sumamos el tiempo de espera de este cliente al total
        Ttotal += acumulado
        
        NCliente += 1

    # Calculamos el tiempo medio de espera por cliente
    TMedio = Ttotal / numTrabajos
    # ====================
    
    print("\n--- Resultado Final de la Simulación ---")
    print(f"Tiempo de espera TOTAL: {Ttotal} minutos")
    print(f"Tiempo de espera MEDIO: {TMedio:.2f} minutos")


if __name__ == "__main__":
    main()
    

