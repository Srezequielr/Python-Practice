import numpy as np
from lista import Lista

class HashEncadenado:
    __hash: np.array
    __tamanio: int
    def __init__(self, clavesEsperadas = 100, promColiciones = 2):
        self.__tamanio = round(self.proxPrim(clavesEsperadas / promColiciones))
        self.__hash = np.array([Lista() for _ in range(self.__tamanio)], dtype = Lista)

    # ===== Insertar =====
    def insertar(self, clave):
        claveHash = self.transformacion(clave)
        self.__hash[claveHash].insertar(clave)
    # ====================

    # ===== Buscar =====
    def buscar(self, clave):
        claveHash = self.transformacion(clave)
        encontrado = self.__hash[claveHash].buscar(clave)
        if(encontrado):
            print("Elemento encontrado.")
        else: 
            print("Elemento no encontrado.")
    # ====================

    # ===== Transformacion clave =====
    def transformacion(self, clave):
        return clave % self.__tamanio
    # ====================

    # ===== Revisa si el numero es primo o no =====
    def primo(self, numero):
        if(numero <= 1):
            return False
        for i in range(2, int(numero**0.5) + 1):
            if numero % i == 0:
                return False
        return True
    # ====================
    
    # ===== Encuentra el primo de un numero =====
    # Usa la funcion primo
    def proxPrim(self, numero):
        while not self.primo(numero):
            numero += 1
        return numero
    # ====================

    # ===== Recorrer tabla Hash =====
    def recorrerHash(self):
        i = 0 
        while i < self.__tamanio:
            print(f"Fila {i:02d}: [ {i} ]")
            self.__hash[i].recorrer()
            i += 1
    # ====================
