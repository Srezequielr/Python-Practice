import csv 
from claEmpleado import Empleado

class ManejadorEmpleado:
    __empleados: list 
    def __init__(self):
        self.__empleados = []
    def cargarEmpleado(self, nombre, idEmp, puesto):
        empleado = Empleado(nombre, idEmp, puesto)
        self.__empleados.append(empleado)
    def cargarCSV(self):
        bandera = True
        archivo = open("empleados.csv", "r", encoding = "UTF-8")
        reader = csv.reader(archivo, delimiter = ";")
        for fila in reader:
            if bandera:
                bandera = False
            else:   
                nombre = fila[0]
                idEmp = int(fila[1])
                puesto = fila[2]
                self.cargarEmpleado(nombre, idEmp, puesto)
    def obtEmpleados(self):
        return self.__empleados
    def buscarEmpleado(self, nomEmp):
        encontrado = False
        i = 0
        resultado = False
        cantidad = len(self.__empleados)
        while not encontrado and i < cantidad:
            if nomEmp == self.__empleados[i].obtNomAp():
                resultado = self.__empleados[i]
                encontrado = True
            i += 1
        return resultado

                