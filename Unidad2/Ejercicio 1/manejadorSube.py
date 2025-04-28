from claseSube import Sube
class ManejadorSube:
    def __init__(self):
        self.__lista = []
    def agregarSube(self, numero):
        unSube = Sube(numero)
        self.__lista.append(unSube)
    def cargarSaldo(self, monto, numero):
        if monto < 0:
            return "Monto inválido"
        for sube in self.__lista:            
            if sube.getNumero() == numero:
                sube.cargar(monto)
                return "Carga existosa"
    def pagarPasaje(self, tarifa, numero):
        for sube in self.__lista:
            if sube.getNumero() == numero:
                if sube.getSaldo() - tarifa >= -500:
                    sube.cargar(-tarifa)
                    return "Pasaje pagado con éxito, saldo restante: " + str(sube.getSaldo())
                else:
                    return "Saldo insuficiente para pagar el pasaje."
        return "El número de tarjeta no existe."
    def verTarjetas(self):
        for sube in self.__lista:
            print("Numero de tarjeta: ", sube.getNumero(), ", Saldo: ", sube.getSaldo())
    def verSaldoNeg(self):
        for sube in self.__lista:
            if sube.getSaldo() < 0:
                print("Numero de tarjeta: " + sube.getSaldo())