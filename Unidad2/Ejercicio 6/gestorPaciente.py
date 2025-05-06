from clasePaciente import Paciente
import csv
class GestorPaciente:
    __listaPacientes: list
    def __init__(self):
        self.__listaPacientes = []
    def cargarLista(self):
        encontrado = True
        with open("pacientes.csv", "r", encoding="utf-8") as archivoPacientes:
            reader = csv.reader(archivoPacientes, delimiter=";")
            for fila in reader:
                if encontrado:
                    encontrado = not encontrado
                else:
                    paciente = Paciente(int(fila[0]), fila[1], fila[2])
                    self.__listaPacientes.append(paciente)
    