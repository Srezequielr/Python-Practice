from claseSube import Sube
class ManejadorSube:
    def __init__(self):
        self.__lista = []
    def agregarSube(self, numero):
        nuevaSube = Sube(numero)
        self.__lista.append(nuevaSube)
    def cargarSaldo(self, numero, monto):
        encontrado = None
        i = 0
        retorno = -1
        if monto <= 0:
            encontrado = True
            retorno = -1
        while not encontrado and i < len(self.__lista):
            if self.__lista[i].verNumero() == numero:   
                retorno = self.__lista[i].cargarSaldo(monto)
                encontrado = True
            else:
                i+=1
        return retorno
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
                print("Numero de tarjeta: " + Sube.getSaldo())

