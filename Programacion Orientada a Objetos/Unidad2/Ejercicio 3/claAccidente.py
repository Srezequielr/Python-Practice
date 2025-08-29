import numpy as np
class Accidente:
    __arrayAccidentes = np.array
    def __init__(self, numDeptos = 19):
        self.__arrayAccidentes = np.empty((numDeptos, 12), dtype = int)
    