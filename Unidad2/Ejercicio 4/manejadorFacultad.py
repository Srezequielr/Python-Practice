import csv
import numpy as np
from claFacultad import Facultad

class ManejadorFacultad:
    __arrayFacultades: np.array
    __incremento: int
    __dimencion: int
    __cantidad: int
    def __init__(self, dimencion = 6):
        self.__dimencion = dimencion
        self.__incremento = 5
        self.__cantidad = 0
        self.__arrayFacultades = np.empty(self.__dimencion, dtype=Facultad)
    def cargarFacultad(self, facultad: Facultad):
        if (self.__dimencion == self.__cantidad):
            self.__dimencion += self.__incremento
            self.__arrayFacultades = np.resize(self.__arrayFacultades, self.__dimencion)
            self.__arrayFacultades[self.__cantidad] = facultad
            self.__cantidad += 1
        else:
            self.__arrayFacultades[self.__cantidad] = facultad
            self.__cantidad += 1
    def cargarDatos(self):
        bandera = True 
        archivo = open('Facultades.csv')
        reader = csv.reader(archivo, delimiter=";")
        for fila in reader:
            if(bandera):
                bandera = not bandera
            else:
                facultad = Facultad(int(fila[0]), fila[1], fila[2], fila[3], fila[4])
                self.cargarFacultad(facultad)
    def mostrarFacultad(self, idFacultad):
        encontrado = False
        i = 0
        print(f"ID: {idFacultad}")
        while i < self.__cantidad and not encontrado:
            if (self.__arrayFacultades[i].obtIdFacultad() == idFacultad):
                encontrado = True
            else:
                i += 1
        if (encontrado):
            return self.__arrayFacultades[i].obtNombre()
        else:
            print("No se encontro la facultad")
    def obtenerFacultades(self):
        return self.__arrayFacultades