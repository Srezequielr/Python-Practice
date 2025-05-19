import csv 
from claTramo import Tramo
from manejadorColectivo import ManejadorColectivo

class manejadorTramo:
    __lista: list
    __manCol: ManejadorColectivo
    def __init__(self, manCol):
        self.__lista = []
        self.__manCol = manCol
    def cargarTramo(self, tramo: Tramo):
        self.__lista.append(tramo)
    def cargarDatos(self):
        bandera = True
        archivo = open("tramos.csv")
        reader = csv.reader(archivo, delimiter = ";")
        for fila in reader:
            if(bandera):
                bandera = not bandera
            else:
                tramo = Tramo(fila[0], fila[1], float(fila[2]), fila[3])
                self.cargarTramo(tramo)
    def listaTramos(self, dniChofer):
        patente = self.__manCol.buscarDNI(dniChofer).obtPatente()
        km = 0
        
        for i in range(len(self.__lista)):
            if(self.__lista[i].obtPatente() == patente):
                km += self.__lista[i].obtDistancia()
                print(self.__lista[i])
        
        
        
    