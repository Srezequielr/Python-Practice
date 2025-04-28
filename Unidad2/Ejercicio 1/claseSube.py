class Sube:
    def __init__(self,  numero = 0, saldo = 0):
        self.__saldo = saldo
        self.__numero = numero
    def getSaldo(self):
        return self.__saldo
    def getNumero(self):
        return self.__numero
    def cargar(self, monto):
        self.__saldo += monto