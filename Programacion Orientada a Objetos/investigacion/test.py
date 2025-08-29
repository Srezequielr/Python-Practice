from clase_producto import Producto
from arreglo_numpy import ManejadorArreglo
def test():
    unManejador=ManejadorArreglo(3)
    unManejador.test()
    unManejador.incremento(2.4)
    unManejador.mostrarElementos()
if __name__=='__main__':
    test()