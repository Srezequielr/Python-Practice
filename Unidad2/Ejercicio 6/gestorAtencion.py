from claseAtencion import Atencion
import csv
import numpy as np
class GestorAtencion:
    __arreAtencion: np.array
    __dimension: int
    __incremento: int
    __cantidad: int
    def __init__(self, dimension = 50, incremento = 10 ):
        self.__arreAtencion = np.empty(self.__dimension, dtype=Atencion)
        self.__dimension = dimension
        self.__incremento = incremento
        self.__cantidad = 0
    
        