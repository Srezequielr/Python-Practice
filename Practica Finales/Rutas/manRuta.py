import csv
from claRuta import Ruta

class ManejadorRuta:
    __rutas: list
    def __init__(self):
        self.__rutas
    def cargaCSV(self):
        archivo = open("Rutas.csv", "r")
        reader = csv.reader(archivo)
        primero = True
        for fila in reader:
            if(primero):
                primero = False
            else:
                ruta = Ruta(int(fila[0]), fila[1], int(fila[2]), fila[3].strip().lower() != "falso")
                self.__rutas.append(ruta)
        archivo.close()
    def buscarRuta(self, codRuta):
        encontrado = False
        i = 0
        resultado = None
        longitud = len(self.__rutas)
        
        while not encontrado and i < longitud:
            if (self.__rutas.getCod() == codRuta):
                encontrado = True 
                resultado = self.__rutas[i]
            i += 1
        return resultado
    def asignarRuta(self):
        codRuta = int(input("Ingrese codigo de ruta: "))
        ruta = self.buscarRuta(codRuta)
        resultado = None
        
        if(ruta):
            if(ruta.getAsignada()):
               resultado = -1
            else:
                ruta.asigRuta()
                resultado = 0
        else:
            resultado = -2
        return resultado