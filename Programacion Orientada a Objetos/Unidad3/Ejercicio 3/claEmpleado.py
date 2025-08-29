class Empleado:
    __nomAp: str
    __idEmpleado: int
    __puesto: str
    def __init__(self, nomAp = "", idEmpleado = "", puesto = ""):
        self.__nomAp = nomAp
        self.__idEmpleado = idEmpleado
        self.__puesto = puesto
    def obtNomAp(self):
        return self.__nomAp
    def obtIdEmpleado(self):
        return self.__idEmpleado
    def obtPuesto(self):
        return self.__puesto
    def __str__(self):
        return f"Nombre y Apellido: {self.__nomAp} "