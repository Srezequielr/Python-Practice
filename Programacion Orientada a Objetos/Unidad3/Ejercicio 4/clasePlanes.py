class Plan:
    __compania: str
    __duracion: int
    __cobertura: str
    __precioBase: float
    def __init__(self, compania, duracion, cobertura, precioBase):
        self.__compania = compania
        self.__duracion = duracion
        self.__cobertura = cobertura
        self.__precioBase = precioBase
    def getCompania(self):
        return self.__compania
    def getDuracion(self):
        return self.__duracion
    def getCobertura(self):
        return self.__cobertura
    def getPrecioBase(self):
        return self.__precioBase
    def __str__(self):
        return f"{self.__class__.__name__:<15}{self.getCompania():<19}{self.getDuracion():<11}{self.getCobertura():<27}{self.getPrecioBase():.2f}"
        # self.__class__.__name__ devuelve el nombre de la clase
    
    