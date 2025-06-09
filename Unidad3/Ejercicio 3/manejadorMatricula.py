import csv
from manejadorEmpleado import ManejadorEmpleado
from manejadorProgCapacitacion import ManejadorProgCapacitacion
from claMatricula import Matricula

class ManejadorMatricula:
    __matriculas: list
    __manEmpleado: ManejadorEmpleado
    __manPrograma: ManejadorProgCapacitacion
    def __init__(self, manEmpleado, manPrograma):
        self.__manEmpleado = manEmpleado
        self.__manPrograma = manPrograma
        self.__matriculas = []
    def cargarMatricula(self, fecha, empleado, programa):
        matricula = Matricula(fecha, empleado, programa)
        self.__matriculas.append(matricula)
    def cargaCSV(self):
        bandera = True
        archivo = open("matriculas.csv", "r", encoding="UTF-8")
        reader = csv.reader(archivo, delimiter= ";")
        for fila in reader:
            if bandera: 
                bandera = False
            else:
                fecha = fila[0]
                empleado = self.__manEmpleado.buscarEmpleado(fila[1])
                programa = self.__manPrograma.buscarPrograma(fila[2])
                self.cargarMatricula(fecha, empleado, programa)
    def verProgramasPorEmpleado(self, idEmpleado):
        print(f"Duracion de los programas del empleado: {idEmpleado}")
        cont = 0
        for matricula in self.__matriculas:
            if matricula.obtEmpleado().obtIdEmpleado() == idEmpleado:
                cont += 1
                print(f"- Duracion: {matricula.obtPrograma().obtDuracion()}")
        if cont == 0:
            print("Empleado inexistente o sin matriculas")
    def verMatriculados(self, nomProg):
        print("Lista de matriculados")
        cont = 0
        for matricula in self.__matriculas: 
            if matricula.obtPrograma().obtNombre() == nomProg:
                cont += 1
                print(f"- {matricula.obtEmpleado().obtNomAp()}")
        if cont == 0:
            print("Programa inexistente o sin empleados")
    def verEmpleadosSinMatricula(self):
        listEmpleados = []
        i = 0
        encontrado = False
        empleados = self.__manEmpleado.obtEmpleados() 
        
        for empleado in empleados:
            listEmpleados.append(empleado.obtNomAp())
        
        longitud = len(self.__matriculas)
        print("Empleado sin ninguna matricula: ")
        for empleado in listEmpleados:
            cant = 0
            while not encontrado and i < longitud:
                if empleado == self.__matriculas[i].obtEmpleado().obtNomAp():
                    cant += 1
                i += 1
            if cant == 0:
                print(empleado)
            cant = 0
            i = 0
        
        
        