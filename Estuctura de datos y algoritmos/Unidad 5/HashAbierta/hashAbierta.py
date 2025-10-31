import numpy as np

class HashAbierto:
    __hash: np.array
    __tamanio: int
    __inserciones: int
    def __init__(self, clavesEsperadas = 100, FCarga = 0.7):
        self.__tamanio = round(self.proxPrim(clavesEsperadas / FCarga))
        self.__hash = np.zeros(self.__tamanio, dtype = int)
        self.__inserciones = 0

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

    # ===== Transformar a clave hash =====
    def transformacion(self, clave):
        return clave % self.__tamanio
    # ====================

    # ===== Inserta un numero =====
    def insertar(self, clave):
        claveHash = self.transformacion(clave)
        
        if(self.__hash[claveHash] == 0):
            self.__hash[claveHash] = clave
            self.__inserciones += 1
        else:
            i = claveHash
            j = 0
            while self.__hash[i] != 0 and j < self.__tamanio:
                i = (i + 1) % self.__tamanio
                j += 1
            if(j == self.__tamanio):
                print("Tabla llena.")
            else:
                self.__hash[i] = clave
                self.__inserciones += 1
    # ====================

    # ===== Buscar en en la tabla hash =====
    def buscar(self, clave):
        claveHash = self.transformacion(clave)

        if(self.__hash[claveHash] == clave):
            print("Clave encontrada por acceso hash.")
        else:
            i = claveHash
            j = 0
            while self.__hash[i] != clave and j < self.__tamanio:
                i = (i + 1) % self.__tamanio
                j += 1
            if(j == self.__tamanio):
                print("Elemento no encontrado.")
            else:
                print("Clave entrontrada por acceso secuencial.") 
    # ====================
    

    # ===== Recorrer Hash Abierto =====
    def recorrer(self):
        for i in range(self.__tamanio):
             print(f"Fila {i:02d}: [ {self.__hash[i]} ]")
    # ====================

    # ===== Obt inserciones =====
    def obtInserciones(self):
        return self.__inserciones
    # ====================