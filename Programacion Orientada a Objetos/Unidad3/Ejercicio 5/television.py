from claMedio import Medio

class Television(Medio):
    __cantCanales: int
    __canales: list
    def __init__(self, nombre, frecuencia, audiencia, cantCanales):
        super().__init__(nombre, frecuencia, audiencia)
        self.__cantCanales = cantCanales
        self.__canales = []
        
    