import csv
from claProgramaCapacitacion import ProgramaCapacitacion

class ManejadorProgCapacitacion:
    __capacitaciones: list
    def __init__(self):
        self.__capacitaciones = []
    def cargaCapacitacion(self, nombre, codigo, duracion):
        programa = ProgramaCapacitacion(nombre, codigo, duracion)
        self.__capacitaciones.append(programa)
    def cargaCSV(self):
        bandera = True
        archivo = open("programas.csv", "r", encoding="UTF-8")
        reader = csv.reader(archivo, delimiter=";")     
        for fila in reader:
            if bandera:
                bandera = False
            else: 
                nombre = fila[0]
                codigo = fila[1]
                duracion = fila[2]
                self.cargaCapacitacion(nombre, codigo, duracion)
    def buscarPrograma(self, nomCap):
        encontrado = False
        i = 0
        resultado = False
        cantidad = len(self.__capacitaciones)
        while not encontrado and i < cantidad:
            if nomCap == self.__capacitaciones[i].obtNombre():
                resultado = self.__capacitaciones[i]
                encontrado = True
            i += 1
        return resultado
                