import csv 
import numpy as np
from claResultado import Resultado
from manejadorEquipo import ManejadorEquipo

class manejadorResultado:
    __arregloResultados: np.array
    __dimencion: int
    __cantidad: int
    __incremento: int
    __manEquipo: ManejadorEquipo
    def __init__(self, manEquipo, dimencion = 16, incremento = 5):
        self.__dimencion = dimencion
        self.__incremento = incremento
        self.__cantidad = 0
        self.__manEquipo = manEquipo
        self.__arregloResultados = np.empty(self.__dimencion, dtype=Resultado)
    def agregarResultado(self, resultado: Resultado):
        if self.__cantidad == self.__dimencion:
            self.__dimencion += self.__incremento
            self.__arregloResultados.resize(self.__dimencion)
        self.__arregloResultados[self.__cantidad] = resultado
        self.__cantidad += 1
    def cargarDatosResultados(self):
        bandera = True
        archivo = open("resultadosLiguilla.csv")
        reader = csv.reader(archivo, delimiter = ";")
        for fila in reader:
            if bandera:
                bandera = not bandera
            else:
                resultado = Resultado(fila[0], fila[1], int(fila[2]), fila[3], int(fila[4]))
                self.agregarResultado(resultado)
    def verResultadosFecha(self):
        fecha = input("ingrese fecha a buscar DD/M/AAAA: ")
        local = 0
        visitante = 0 
        denominacionLocal = 0
        denominacionVisitante = 0
        for i in range(self.__cantidad):
            if self.__arregloResultados[i].obtFecha() == fecha:
                denominacionLocal = self.__manEquipo.obtDenominacion(self.__arregloResultados[i].obtIdEquipoLocal())
                denominacionVisitante = self.__manEquipo.obtDenominacion(self.__arregloResultados[i].obtIdEquipoVisitante())
                local = self.__arregloResultados[i].obtenerGolesLocal()
                visitante = self.__arregloResultados[i].obtenerGolesVisitante()
                print(f"Fecha: {fecha}")
                print(f"Equipo Local: {denominacionLocal} - Goles: {local}")
                print(f"Equipo Visitante: {denominacionVisitante} - Goles: {visitante}")
        if denominacionLocal == 0:
            print("No se encontraron resultados para la fecha ingresada")
    def verResultadosLocalEquipo(self):
        nomEquipo = input("Ingrese el nombre del equipo: ")
        idEquipo = self.__manEquipo.obtIdEquipo(nomEquipo) 
        if idEquipo == 0:
            print("No se encontro el equipo")
        else: 
            for i in range(self.__cantidad):
                if self.__arregloResultados[i].obtIdEquipoLocal() == idEquipo:
                    denominacionVisitante = self.__manEquipo.obtDenominacion(self.__arregloResultados[i].obtIdEquipoVisitante())
                    local = self.__arregloResultados[i].obtenerGolesLocal()
                    visitante = self.__arregloResultados[i].obtenerGolesVisitante()
                    print(f"Fecha: {self.__arregloResultados[i].obtFecha()}")
                    print(f"{nomEquipo} VS {denominacionVisitante}: {local} - {visitante}")
    def cargarTablaPosiciones(self):
        for i in range(self.__cantidad):
            idEquipoLocal = self.__arregloResultados[i].obtIdEquipoLocal()
            idEquipoVisitante = self.__arregloResultados[i].obtIdEquipoVisitante()
            golesLocal = self.__arregloResultados[i].obtenerGolesLocal()
            golesVisitante = self.__arregloResultados[i].obtenerGolesVisitante()
            if golesLocal > golesVisitante:
                self.__manEquipo.agregarVictoria(idEquipoLocal)
            elif golesLocal < golesVisitante:
                self.__manEquipo.agregarVictoria(idEquipoVisitante)
            else:
                self.__manEquipo.agregarEmpate(idEquipoLocal)
                self.__manEquipo.agregarEmpate(idEquipoVisitante)
            self.__manEquipo.agregarGolesAFavor(idEquipoLocal, golesLocal)
            self.__manEquipo.agregarGolesAFavor(idEquipoVisitante, golesVisitante)
            self.__manEquipo.agregarGolesEnContra(idEquipoLocal, golesVisitante)
            self.__manEquipo.agregarGolesEnContra(idEquipoVisitante, golesLocal)
            self.__manEquipo.actualizarDiferenciaGoles(idEquipoLocal)
            self.__manEquipo.actualizarDiferenciaGoles(idEquipoVisitante)
        
        
