from claseSube import Sube
class ManejadorSube:
    def __init__(self):
        self.__lista = []
    def agregarSube(self, numero):
        nuevaSube = Sube(numero)
        self.__lista.append(nuevaSube)
    def cargarSaldo(self, numero, monto):
        if monto <= 0:
            return "Monto inválido"
        for Sube in self.__lista:
            if Sube.verNumero() == numero:
                return "Carga exitosa, saldo restante: " + str(Sube.cargarSaldo(monto))
        return "Tarjeta no encontrada"
    def pagarPasaje(self, numero, tarifa):
        for Sube in self.__lista:
            if Sube.verNumero() == numero:
                if Sube.pagarPasaje(tarifa) == -1:
                    return "Saldo insuficiente"
                else:
                    return "Pago realizado, saldo restante es " + str(Sube.verSaldo()) 
    def verSaldo(self, numero):
        for Sube in self.__lista:
            if Sube.verNumero() == numero:
                return "Saldo: " + str(Sube.verSaldo())
            else:
                return "Sube no encontrada"
    def verSubesNeg(self):
        for Sube in self.__lista:
            if Sube.verSaldo() < 0:
                print("Numero de tarjeta: " + sube.getSaldo())

