import csv
from claseTelefonia import Telefonia
from claseTelevision import Television

class ManejadorPlanes:
    __planes: list
    def __init__(self):
        self.__planes = []
        
    def agregarTelefonia(self, compania, duracion, cobertura, precioBase, tipoLlamada, minutos):
        telefonia = Telefonia(compania, duracion, cobertura, precioBase, tipoLlamada, minutos)
        self.__planes.append(telefonia)
        
    def agregarTelevision(self, compania, duracion, cobertura, precioBase, canalesInt, canalesNac):
        television = Television(compania, duracion, cobertura, precioBase, canalesInt, canalesNac)
        self.__planes.append(television)
        
    def cargaCSV(self):
        archivo = open("planes.csv", "r")
        reader = csv.reader(archivo, delimiter=";")
        primero = True
        for fila in reader:
            if(primero):
                primero = False
            else:
                if(fila[0] == 'T'):
                    self.agregarTelevision(fila[1], int(fila[2]), fila[3], float(fila[4]), int(fila[5]), int(fila[6]))
                elif(fila[0] == "M"):
                    self.agregarTelefonia(fila[1], int(fila[2]), fila[3], float(fila[4]), fila[5], int(fila[6]))
                else:
                    print("Hay un dato invalido en el CSV.")
                    
    def verTipoPlan(self):
        indice = int(input("Ingrese numero de plan: "))
        
        if(isinstance(self.__planes[indice], Telefonia)):
            print("Este es un plan de telefonia.")
        elif(isinstance(self.__planes[indice], Television)):
            print("Este es un plan de television.")
        else:
            print("Desconocido.")  
             
    def verPlanesXcobertura(self):
        cobertura = input("Ingesar cobertura geografica: ")             
        cont = 0
        
        for plan in self.__planes:
            if(plan.getCobertura() == cobertura):
                cont += 1
        
        print(f"Hay {cont} en el area de cobertura selccionada.")
        
    def verPlanesInt(self):
        cantCanales = int(input("Ingresar numero de canales internacionales: "))
        
        for plan in self.__planes:
            if(isinstance(plan, Television)):
                if(plan.getCanalesInt() >= cantCanales):
                    print(plan.getCompania())
    
    def listarPlanes(self):
        print(f"{'Tipo de Plan:':<15}{'Compañia:':<19}{'Duración:':<11}{'Cobertura:':<27}{'Precio final:'}")
        for plan in self.__planes:
            print(plan)
        
                    
            