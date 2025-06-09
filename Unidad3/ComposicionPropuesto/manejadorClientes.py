import csv
from claCliente import Cliente 

class ManejadorClientes:
    __listaClientes: list
    def __init__(self):
        self.__listaClientes = []
    def agregarCliente(self, dni, nombre, apellido):
        cliente = Cliente(dni, nombre, apellido)
        self.__listaClientes.append(cliente)
    def buscarCliente(self, dni):
        encontrado = False
        i = 0
        result = False
        cantidad = len(self.__listaClientes)
        while not encontrado and i < cantidad:
            if self.__listaClientes.obtDni() == dni:
                result = self.__listaClientes[i]
                encontrado = True
            i += 1
        return result
    def agregarMascota(self, dni, nombre, especie, edad):
        cliente = self.buscarCliente(dni)
        if cliente:
            cliente.agregarMascota(dni, nombre, especie, edad)
    def cargarCSVClientes(self):
        bandera = True
        