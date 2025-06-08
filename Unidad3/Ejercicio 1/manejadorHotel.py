import csv
from claHotel import Hotel
from claHabitacion import Habitacion

class ManejadorHotel:
    __hoteles: list
    def __init__(self):
        self.__hoteles = []
    def cargarDatos(self):
        archivo = open("Hoteles.csv", "r", encoding="UTF-8")
        reader = csv.reader(archivo, delimiter = ";")
        for fila in reader:
            if(len(fila) == 3):
                hotel = Hotel(fila[0], fila[1], fila[2])
                self.__hoteles.append(hotel)
            if(len(fila) == 5):
                hotel.agregarHabitacion(int(fila[0]), int(fila[1]), fila[2], float(fila[3]), fila[4].strip().lower() == "true")               
    def buscarHotel(self):
        nomHotel = input("Ingrese nombre del hotel: ")
        encontrado = False
        resultado = bool
        i = 0
        while not encontrado and i < len(self.__hoteles):
            if nomHotel == self.__hoteles[i].obtNombre():
                resultado = self.__hoteles[i]
                encontrado = True
            i += 1
        if not encontrado:
            resultado = False
        return resultado            
    def agregarHabitacion(self):
        hotel = self.buscarHotel()      
        if hotel:
            numero = int(input("Ingese numero de la habitacion: "))
            piso = int(input("Ingrese piso donde esta la habitacion: "))
            tipo = input("Ingrese tipo de la habitacion: ")
            precio = float(input("Ingese precio de la habitacion: "))
            hotel.agregarHabitacion(numero, piso, tipo, precio)
        else:
            print("Hotel no encontrado")   
    def reservarHabitacion(self):
        hotel = self.buscarHotel()       
        if hotel:
            numHab = int(input("Ingrese numero de habitacion: "))
            habitacion = hotel.obtHabitacion(numHab)
            if not habitacion:
                print("Habitacion no encontrada")
            else:
                if not habitacion.reservar():
                    print("Habitacion Ocupada o no disponible")
                else:
                    print("Habitacion reservada con exito")
        else:
            print("Hotel no encontrado")
    def liberarHabitacion(self):
        hotel = self.buscarHotel()
        if hotel:
            numHab = int(input("Ingrese numero de habitacion: "))
            habitacion = hotel.obtHabitacion(numHab)
            if not habitacion:
                print("Habitacion no encontrada")
            else:
                if not habitacion.liberar():
                    print("Habitacion ya estaba liberada")
                else:
                    print("Habitacion liberada con exito")
        else:
            print("Hotel no encontrado")
    def mostrarHabXTipo(self):
        hotel = self.buscarHotel()
        cont = 0
        if hotel:
            habitaciones = hotel.obtHabitaciones()
            tipoHabitacion = input("Ingese tipo de habitacion: ")
            i = 0
            while i < len(habitaciones): #preguntar en consulta sobre esto, porque puedo recorrer la lista de habitaicones con while y no con for en la forma for habitacion in range(len(habitaciones)) 
                if tipoHabitacion == habitaciones[i].obtTipo():
                    cont += 1
                    print(habitaciones[i])
                i += 1
            if cont == 0:
                print("Ningun tipo de habitacion coincide con el ingresado")
        else:
            print("Hotel no encontrado")
    def mostrarHabLibres(self):
        hotel = self.buscarHotel()
        cont = 0 
        bandera = False
        i = 0
        if hotel:
            habitaciones = hotel.obtHabitaciones()
            piso = int(input("Ingrese numero de piso: "))
            while i < len(habitaciones):
                if piso == habitaciones[i].obtPiso():
                    bandera = True
                    if habitaciones[i].obtDispo():
                        cont += 1
                i += 1
            if bandera:
                print(f"Las habitaciones libres en el piso {piso} son: {cont}")
            else:
                print("Piso invalido")
        else: 
            print("Hotel no encontrado")
    def listaHab(self):
        hotel = self.buscarHotel()
        tipos = []
        i = 0
        j = 0
        if hotel:
            habitaciones = hotel.obtHabitaciones()
            cantidad = len(habitaciones)
            while i < cantidad:
                tipos.append(habitaciones[i].obtTipo()) 
                i+=1
            tipos = list(set(tipos))
            i = 0
            while j < len(tipos):
                print(f"Tipo_de habitacion: {tipos[j]}")
                print(f"{"Numero":<15}{"Piso":<10}{"Precio":<20}{"Disponibilidad":<15}")
                while i < cantidad:
                    if tipos[j] == habitaciones[i].obtTipo():
                       print(habitaciones[i].mostrarHabitacion())
                    i += 1
                j += 1
                i = 0
                print("\n") 
        else: 
            print("Hotel no encontrado")

            
            # while j < len(tipos):
            #     print(f"Tipo_de habitacion: {tipos[j]}")
            #     print(f"{"Numero":<15}{"Piso":<10}{"Precio":<20}{"Disponibilidad":<15}")
            #     while i < cantidad:
            #         if tipos[j] == habitaciones[i].obtTipo():
            #             habitaciones[i].mostrarHabitacion()
            #         i += 1
            #     j += 1
            #     print("\n")      
    
            
            
            
            # while i < cantidad:
            #     print(f"Tipo_de habitacion: {tipos[j]}")
            #     print(f"{"Numero":<15}{"Piso":<10}{"Precio":<20}{"Disponibilidad":<15}")
            #     while j < len(tipos):
            #         if tipos[j] == habitaciones[i].obtTipo():
            #             print(habitaciones[i].mostrarHabitacion())
            #         j += 1 
            #     j = 0  
            #     i += 1  
            #     print("\n")  
        