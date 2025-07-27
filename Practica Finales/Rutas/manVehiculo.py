from claAutomovil import Automovil
from claCamion import Camion
from Lista import Lista

class ManejadorVehiculo:
    __vehiculos: Lista
    __manRuta: object
    def __init__(self, manRuta):
        self.__vehiculos = Lista()
        self.__manRuta = manRuta
    def agregarAutomovil(self, automovil):
        self.__vehiculos.agregarNodo(automovil)
    def agregarCamion(self, camion):
        self.__vehiculos.agregarNodo(camion)
    def cargarVehiculos(self):
        tipo = int(input("Que vehiculo va a cargar? (1. auto - 2. camion): "))
        patente = input("Ingrese patente del vehiculo: ")
        modelo = input("Ingrese modelo del vehiculo: ")
        costoXKm = input("Ingrese costo por kilometros del vehiculo: ")
        cantDias = int(input("Ingrese cantidad de dias de alquiler: "))
        
        if(tipo == 1):
            maxPasajeros = int(input("Ingrese cantidad maxima de pasajeros del automovil: "))
            cantPasTransportados = int(input("Ingrese cantidad de pasajeros transportados: "))
            automovil = Automovil(patente, modelo, costoXKm, cantDias, maxPasajeros, cantPasTransportados)
            self.agregarAutomovil(automovil)
        elif(tipo == 2):
            capMaxCarga = int(input("Ingrese capacidad maxima de carga del camion: "))
            cantTransportada = int(input("Ingrese el peso total transportado (Kilogramos): "))
            asignacion = self.__manRuta.asigRuta()
            
            if(asignacion == -1):
                raise IOError
            elif(asignacion == -2):
                raise IndexError
            else:
                camion = Camion(patente, modelo, costoXKm, cantDias, capMaxCarga, cantTransportada)
                self.agregarCamion(camion) 
        else:
            print("Tipo de vehiculo invalido.")
    def mostrarDataVehiculo(self):
        vehiculo = self.__vehiculos.buscarVehiculo()
        if(vehiculo):
            print(vehiculo)
        else:
            raise Exception