##Julian riera


import csv
from claEquipo import Equipo

class ManejadorEquipo:
    __listaEquipos: list
    def __init__(self):
        self.__listaEquipos = []
    def agregarEquipo(self, equipo: Equipo):
        self.__listaEquipos.append(equipo)
    def cargarDatosEquipos(self):
        bandera = True
        archivo = open("equiposLiguilla.csv")
        reader = csv.reader(archivo, delimiter = ";")
        for fila in reader:
            if bandera:
                bandera = not bandera
            else:
                equipo = Equipo(fila[0], fila[1], fila[2], int(fila[3]), int(fila[4]), int(fila[5]), int(fila[6]))
                self.agregarEquipo(equipo)
    def obtDenominacion(self, idEquipo):
        bandera = False
        resultado = 0
        i = 0
        while not bandera and i < len(self.__listaEquipos):
            if self.__listaEquipos[i].obtIdEquipo() == idEquipo:
                bandera = True
                resultado = self.__listaEquipos[i].obtDenominacion()
            else:
                i += 1
        return resultado
    def obtIdEquipo(self, denominacion):
        bandera = False
        i = 0 
        resultado = 0
        while not bandera and i < len(self.__listaEquipos):
            if self.__listaEquipos[i].obtDenominacion() == denominacion:
                bandera = True
                resultado = self.__listaEquipos[i].obtIdEquipo()
            else:
                i += 1
        return resultado
    def agregarVictoria(self, idEquipo):
        i = 0
        bandera = False
        while not bandera and i < len(self.__listaEquipos):
            if self.__listaEquipos[i].obtIdEquipo() == idEquipo:
                self.__listaEquipos[i].victoria()
                bandera = True
            else:
                i += 1
    def agregarEmpate(self, idEquipo):
        i = 0
        bandera = False
        while not bandera and i < len(self.__listaEquipos):
            if self.__listaEquipos[i].obtIdEquipo() == idEquipo:
                self.__listaEquipos[i].empate()
                bandera = True
            else:
                i += 1
    def mostrarTablaPosiciones(self):
        for i in range(len(self.__listaEquipos)):
            print(f"{self.__listaEquipos[i].obtIdEquipo()}\t{self.__listaEquipos[i].obtDenominacion()}\t{self.__listaEquipos[i].obtPuntos() }\t{self.__listaEquipos[i].obtenerGolesAFavor()}\t{self.__listaEquipos[i].obtenerGolesEnContra()}\t{self.__listaEquipos[i].obtenerDiferenciaGoles()}")
    def agregarGolesAFavor(self, idEquipo, goles):
        i = 0
        bandera = False
        while not bandera and i < len(self.__listaEquipos):
            if self.__listaEquipos[i].obtIdEquipo() == idEquipo:
                self.__listaEquipos[i].cargarGolesAFavor(goles)
                bandera = True
            else:
                i += 1
    def agregarGolesEnContra(self, idEquipo, goles):
        i = 0
        bandera = False
        while not bandera and i < len(self.__listaEquipos):
            if self.__listaEquipos[i].obtIdEquipo() == idEquipo:
                self.__listaEquipos[i].cargarGolesEnContra(goles)
                bandera = True
            else:
                i += 1
    def actualizarDiferenciaGoles(self, idEquipo):
        i = 0
        bandera = False
        while not bandera and i < len(self.__listaEquipos):
            if self.__listaEquipos[i].obtIdEquipo() == idEquipo:
                self.__listaEquipos[i].actualizarDiferenciaGoles()
                bandera = True
            else:
                i += 1
    def ordenar(self):
        self.__listaEquipos.sort()
        print("Tabla de posiciones ordenada")