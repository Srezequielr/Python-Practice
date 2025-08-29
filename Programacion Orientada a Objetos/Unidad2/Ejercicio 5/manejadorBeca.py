import csv
import numpy as np
from claBeca import Beca

class ManejadorBeca:
    __arregloBecas: np.array
    __cantidad: int
    __dimension: int
    __incremento: int
    def __init__(self, dimension = 6, incremento = 5):
        self.__dimension = dimension
        self.__incremento = incremento
        self.__cantidad = 0
        self.__arregloBecas = np.empty(self.__dimension, dtype = Beca)
    def agergarBeca(self, beca: Beca):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__arregloBecas.resize(self.__dimension)
        self.__arregloBecas[self.__cantidad] = beca
        self.__cantidad += 1
    def cargarDatos(self):
        bandera = True
        archivo = open("becas.csv")
        reader = csv.reader(archivo, delimiter = ";")
        for fila in reader:
            if bandera:
                bandera = not bandera
            else:
                beca = Beca(int(fila[0]), fila[1], float(fila[2]))
                self.agergarBeca(beca)