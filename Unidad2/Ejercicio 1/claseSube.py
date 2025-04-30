class Sube:
    def __init__(self,  numero = 0, saldo = 0):
        self.__saldo = saldo
        self.__numero = numero
    def cargarSaldo(self, importe):
        self.__saldo += importe
        return self.__saldo
    def pagarPasaje(self, tarifa):
        if self.__saldo - tarifa <= -200:
            return -1
        else:
            return self.cargarSaldo(-tarifa)
    def verSaldo(self):
        return self.__saldo
    def verNumero(self):
        return self.__numero
        