import csv
from claBeneficiario import Beneficiario

class ManejadorBeneficiario:
    __listaBeneficiarios: list
    def __init__(self):
        self.__listaBeneficiarios = []
    def agregarBeneficiario(self, beneficiario: Beneficiario):
        self.__listaBeneficiarios.append(beneficiario)
    def cargarDatos(self):
        bandera = True
        archivo = open("beneficiarios.csv")
        reader = csv.reader(archivo, delimiter = ";")
        for fila in reader:
            if bandera:
                bandera = not bandera
            else:
                beneficiario = Beneficiario(fila[0], fila[1], fila[2], fila[3], fila[4], int(fila[5]), float(fila[6]), int(fila[7]))
                self.agregarBeneficiario(beneficiario)
    