class Producto:
    __descripcion: str
    __cantidad: int
    __precioUnitario: float
    def __init__(self, descripcion, cantidad, precioUnitario):
        self.__descripcion=descripcion
        self.__cantidad=cantidad    
        self.__precioUnitario=precioUnitario
    def __add__(self, incremento):
        self.__precioUnitario=self.__precioUnitario*(1+incremento/100)
    def __str__(self):
        return f"descripción: {self.__descripcion}, precio: {self.__precioUnitario}"