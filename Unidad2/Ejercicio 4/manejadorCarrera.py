
import csv
import numpy as np
from claCarrera import Carrera
from manejadorFacultad import ManajedorFacultad

class ManejadorCarrera:
    __arrayCarreras: np.array
    __incremento: int
    __dimencion: int
    __cantidad: int
    __manFac: ManajedorFacultad
    def __init__(self, dimencion=20, manFacultad = ManajedorFacultad):
        self.__dimencion = dimencion
        self.__incremento = 5
        self.__cantidad = 0
        self.__manFac = manFacultad
        self.__arrayCarreras = np.empty(self.__dimencion, dtype=Carrera)
    def cargarCarrera(self, carrera: Carrera):
        if (self.__dimencion == self.__cantidad):
            self.__dimencion += self.__incremento
            self.__arrayCarreras = np.resize(self.__arrayCarreras, self.__dimencion)
            self.__arrayCarreras[self.__cantidad] = carrera
            self.__cantidad += 1
        else:
            self.__arrayCarreras[self.__cantidad] = carrera
            self.__cantidad += 1
    def cargarDatos(self):
        bandera = True 
        archivo = open('Carreras.csv')
        reader = csv.reader(archivo, delimiter=";")
        for fila in reader:
            if(bandera):
                bandera = not bandera
            else:
                carrera = Carrera(int(fila[0]), fila[1], fila[2], fila[3], fila[4], int(fila[5]))
                self.cargarCarrera(carrera)