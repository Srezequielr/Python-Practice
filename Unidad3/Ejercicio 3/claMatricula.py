class Matricula():
    __fecha: str
    __empleado: object
    __programa: object
    def __init__(self, fecha, empleado, programa):
        self.__fecha = fecha
        self.__empleado = empleado
        self.__programa = programa
    def obtFecha(self):
        return self.__fecha
    def obtEmpleado(self):
        return self.__empleado
    def obtPrograma(self):
        return self.__programa