from cola import Cola
import random


def main():
    colaImpresion = Cola()
    ts = 60 # Tiempo total de la simulacion
    tt = 0 # Tiempo transcurrido
    llegadaProm = 5 # Tiempo promedio de llegada cada x minutos
    tiepoMaximo = 3 # Cant de minutos maxima que puede estar un documento imprimiendose, sobrepasado ese lim es desalojado y cargado en cola
    trabajoActual = None # Trabajo que se esta imprimiendo
    canPag = 0 # Candidad de paginas que tiene el documento
    impOcupada = False # Indica si la impresora esta ocupada
    tiemposEspera = [] # Almacena los tiempos de espera de los trabajos terminados

    while tt < ts:
        numRandom = random.random()

        # --------- Evalua si entro un trabajo. ------------
        if(numRandom <= 1 / llegadaProm):
            print("Llego un trabajo.")
            canPag = random.randint(1, 100)
            colaImpresion.insertar(tt, canPag)
        # ---------------------------------------------
        
        # ------------ Si la impresora esta desocupada y hay trabajos en cola, saca un trabajo de cola y van a la impresora. ------------
        if(not impOcupada and not colaImpresion.vacia()):
            print("Tomando servicio...")
            trabajoActual = colaImpresion.suprimir() # Carga el trabajo
            impOcupada = True # Ocupa la impresora
        # ------------------------

        # ------------ Si la impresora esta imprimiendo, entra aca. ------------
        if(impOcupada):
            print("Impresora imprimiendo...")
            tiepoMaximo -= 1 # Reduce el tiempo de impresion
            trabajoActual.setCantPag(trabajoActual.getCanPag() - 10) # Resta la cantidad de paginas que imprimio

            # ------------ Si el trabajo se completo entra ------------
            if(trabajoActual.getCanPag() < 0):
                print("Trabajo terminado.")
                tiemposEspera.append(tt - trabajoActual.getTllegada())
                trabajoActual = None # Desaloja el trabajo
                impOcupada = False # Libera la impresora
                tiepoMaximo = 3 # Reinicia el tiempo
            # ------------ Si alcanzo el limite de impresion, entra. ------------
            elif (tiepoMaximo == 0):
                print("Desalojando trabajo...")
                colaImpresion.insertar(trabajoActual.getTllegada(), trabajoActual.getCanPag())
                trabajoActual = None # Desaloja el trabajo
                impOcupada = False # Libera la impresora
                tiepoMaximo = 3 # Reinicia el tiempo
            # ------------------------------------------------------------
        tt  += 1
    
    print(f"Quedaron sim imprimir {colaImpresion.getCant()} documentos.")

    totalTiempos = 0
    for tiempo in tiemposEspera:
        totalTiempos += tiempo

    promedioEspera = totalTiempos // len(tiemposEspera)

    print(f"El tiempo promedio de espera de los documentos terminados es de: {promedioEspera} Minutos")
        
        


if __name__ == "__main__":
    main()