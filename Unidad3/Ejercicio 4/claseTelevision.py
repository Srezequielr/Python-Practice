from clasePlanes import Plan
class Television(Plan):
    __canalesInt: int
    __canalesNac: int
    def __init__(self, compania, duracion, cobertura, precioBase, canalesInt, canalesNac):
        super().__init__(compania, duracion, cobertura, precioBase)
        self.__canalesInt = canalesInt
        self.__canalesNac = canalesNac
    def getCanalesInt(self):
        return self.__canalesInt
    def getCanalesNac(self):
        return self.__canalesNac
