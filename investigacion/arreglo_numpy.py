from clase_producto import Producto
import numpy as np
class ManejadorArreglo:
    __datos: None
    __cantidad: int
    def __init__(self, cantidad):
        self.__datos=np.empty(cantidad, dtype=Producto)
        self.__cantidad=cantidad
    def test(self):
        unProducto=Producto("Azúcar", 400, 867.50)
        self.__datos[0]=unProducto
        otroProducto=Producto("Harina", 100, 1250)
        self.__datos[1]=otroProducto
        ultimoProducto=Producto("Arroz", 120, 2130)
        self.__datos[2]=ultimoProducto
    def incremento(self,indiceInflacion):
        self.__datos+indiceInflacion
    def mostrarElementos(self):
        for indice in range(self.__cantidad):
            print(self.__datos[indice])
