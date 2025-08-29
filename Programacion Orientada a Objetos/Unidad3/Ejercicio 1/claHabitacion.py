class Habitacion:
    __numero: int
    __piso: int
    __tipo: str
    __precio: float
    __disponibilidad: bool 
    def __init__(self, numero = 0, piso = 0, tipo = "", precio = 0, disponibilidad = True):
        self.__numero = numero
        self.__piso = piso
        self.__tipo = tipo
        self.__precio = precio
        self.__disponibilidad = disponibilidad
    def obtNumero(self):
        return self.__numero
    def obtPiso(self):
        return self.__piso
    def obtTipo(self):
        return self.__tipo
    def obtPrecio(self):
        return self.__precio
    def obtDispo(self):
        return self.__disponibilidad
    def reservar(self):
        result = False
        if self.__disponibilidad:
            self.__disponibilidad = False
            result = True
        return result
    def liberar(self):
        result = False
        if not self.__disponibilidad:
            self.__disponibilidad = True
            result = True
        return result
    def mostrarHabitacion(self):
        return f"{self.__numero:<15}{self.__piso:<10}{self.__precio:<20}{self.__disponibilidad:<15}"
    def __str__(self):
        return f"Numero de habitacion: {self.__numero}\nPiso de habitacion: {self.__piso}"