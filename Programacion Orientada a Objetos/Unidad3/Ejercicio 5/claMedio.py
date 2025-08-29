class Medio:
    __medio: str
    __frecuencia: str
    __audiencia: int 
    def __init__(self, medio, frecuencia, audiencia):
        self.__medio = medio
        self.__frecuencia = frecuencia
        self.__audiencia = audiencia
    def getMedio(self):
        return self.__medio
    def getFrecuencia(self):
        return self.__frecuencia
    def getAudiencia(self):
        return self.__audiencia
        