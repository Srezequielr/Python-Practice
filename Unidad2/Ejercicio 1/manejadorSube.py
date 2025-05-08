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
        encontrado = None
        i = 0
        retorno = -1
        while not encontrado and i < len(self.__lista):
            if self.__lista[i].verNumero() == numero:
                if self.__lista[i].pagarPasaje(tarifa) == -1:
                    retorno = -1
                else:
                    retorno = Sube.verSaldo()  
                encontrado = True
            else:
                i += 1        
        return retorno
    def verSaldo(self, numero):
        encontrado = None
        i = 0
        retorno = -1
        while not encontrado and i < len(self.__lista):
            if self.__lista.verNumero() == numero:
                retorno = self.__lista.verSaldo()
                encontrado = True
            else:
                i += 1
        return retorno 
    def verSubesNeg(self):
        for Sube in self.__lista:
            if Sube.verSaldo() < 0:
                print("Numero de tarjeta: " + Sube.getSaldo())

