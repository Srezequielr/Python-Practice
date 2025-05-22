import csv
import numpy as np
from claColectivo import Colectivo

class ManejadorColectivo:
    __arreglo: np.array
    __cantidad: int
    __incremento: int
    __dimencion: int
    def __init__(self, cantidad = 0, incremento = 3, dimencion = 5):
        self.__arreglo = np.empty(dimencion, Colectivo)
        self.__dimencion = dimencion
        self.__cantidad = cantidad
        self.__incremento = incremento
    def agregarCole(self, cole: Colectivo):
        if (self.__cantidad == self.__dimencion):
            self.__dimencion =+ self.__incremento
            self.__arreglo = np.resize(self.__incremento, self.__incremento)
            self.__arreglo[self.__cantidad] = cole
            self.__cantidad += 1
        else:
            self.__arreglo[self.__cantidad] = cole
            self.__cantidad += 1
    def cargarDatos(self):
        bandera = True
        archivo = open('colectivos.csv', "r")
        reader = csv.reader(archivo, delimiter = ";")
        for fila in reader:
            if(bandera):
                bandera = not bandera
            else:
                cole = Colectivo(fila[0], fila[1], fila[2], int(fila[3]), int(fila[4]))
                self.agregarCole(cole)
    def buscarDNI(self, dni):
        encontrado = None
        i = 0
        retorno = -1
        while not encontrado and i < len(self.__arreglo):
            if(self.__arreglo[i].obtDni() == dni):
                retorno = self.__arreglo[i]
                encontrado = True
            else:
                i += 1
        return retorno
    def obtColectivos(self):
        return self.__arreglo
    def obtPatente(self):
        return self.obtPatente()