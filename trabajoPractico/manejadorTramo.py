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
    def listaTramos(self):
        dniChofer = int(input("Ingrese el DNI del chofer: "))
        patente = self.__manCol.buscarDNI(dniChofer).obtPatente()
        km = 0
        for i in range(len(self.__lista)):
            if(self.__lista[i].obtPatente() == patente):
                km += self.__lista[i].obtDistancia()
                print(self.__lista[i])
        print(f"El chofer {dniChofer} recorrio {km} kilometros")
    def listarColectivos(self):
        colectivos = self.__manCol.obtColectivos()
        for i in range(len(colectivos)):
            km = 0
            for j in range((len(self.__lista))):
                if self.__lista[j].obtPatente() == colectivos[i].obtPatente():
                    km += self.__lista[j].obtDistancia()
                    print(f"Colectivo: {colectivos[i].obtPatente()}, kilometraje: {km}")
            print(f"Se recorrieron en total: {km * 35 / 100} litros de combustible")
    def mostrarTramosMayores(self):
        i=0
        distancia = int(input("Ingrese la distancia: "))
        print("Los tramos mayores a la distancia ingresada son: ")
        for i in range(len(self.__lista)):
            if self.__lista[i].obtDistancia() > distancia:
                print(self.__lista[i])
                print("\n")