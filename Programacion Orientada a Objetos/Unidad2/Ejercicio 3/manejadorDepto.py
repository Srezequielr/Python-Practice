import csv
from claDepto import Depto
from claAccidente import Accidente


class ManejadorDepto:
    __lista = list
    def __init__(self):
        self.__lista = []
    def agregarDepto(self, depto: Depto):
        self.__lista.append(depto)
    def cargarArchivo(self):
        bandera = True
        archivo = open("departamentos.csv")
        reader = csv.reader(archivo, delimiter = ";")
        for fila in reader:
            if(bandera):
                bandera = not bandera
            else:
                depto = Depto(fila[0], int(fila[1]))
                self.agregarDepto(depto)