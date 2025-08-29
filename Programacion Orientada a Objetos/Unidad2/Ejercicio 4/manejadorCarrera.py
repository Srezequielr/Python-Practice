
import csv
import numpy as np
from claCarrera import Carrera
from manejadorFacultad import ManejadorFacultad

class ManejadorCarrera:
    __arrayCarreras: np.array
    __incremento: int
    __dimencion: int
    __cantidad: int
    __manFac: ManejadorFacultad
    def __init__(self,manFacultad = ManejadorFacultad, dimencion = 20):
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
    def mostrarFacultad(self):
        encontrado = False
        carrera = input("Ingrese el nombre de la carrera: ")  
        i = 0   
        while i < self.__cantidad and not encontrado:
            if (self.__arrayCarreras[i].obtNombre() == carrera):
                print(self.__arrayCarreras[i].obtNombre())
                encontrado = True
                print(f"La facultad de la carrera es: {self.__manFac.mostrarFacultad(self.__arrayCarreras[i].obtIdFacultad())}")
            else:
                i += 1
        if (not encontrado):
            print("No se encontro la carrera")
    def contarCarreras(self):
        facultades: ManejadorFacultad = self.__manFac.obtenerFacultades()
        print(facultades[0])
        for i in range(len(facultades)):
            contador = 0
            for j in range(self.__cantidad):
                if (facultades[i].obtIdFacultad() == self.__arrayCarreras[j].obtIdFacultad()):
                    contador += 1
            print(f"La facultad {facultades[i].obtNombre()} tiene {contador} carreras")
    