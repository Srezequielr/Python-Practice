import numpy as np

class HashBucket:
    __tabla: np.array
    __conts: np.array
    __tamanio: int
    __areaPrim: int
    __areaOver: int
    __bucket: int
    def __init__(self, clavEsperadas = 100, bucket = 5):
        self.__tamanio = round(self.proxPrim((clavEsperadas / bucket) * 1.2))  
        self.__areaPrim = round(self.proxPrim(clavEsperadas / bucket))
        self.__areaOver = self.__areaPrim + 1
        self.__bucket = bucket
        self.__tabla = np.zeros((self.__tamanio, bucket), dtype = int)
        self.__conts = np.zeros(self.__tamanio, dtype = int)
    
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
    
    # ===== Trasnformacion de clave a hash (division) =====
    def transformacion(self, clave):
        return int(clave % self.__areaPrim)
    # ====================

    # ===== Insertar un vajor en la tabla =====
    def insertar(self, clave):
        claveHash = self.transformacion(clave)

        if(self.__conts[claveHash] < self.__bucket):
            self.__tabla[claveHash][self.__conts[claveHash]] = clave
            self.__conts[claveHash] += 1
        else:
            i = self.__areaOver
            while  i < self.__tamanio and not self.__conts[i] < self.__bucket:
                i += 1
            if(i == self.__tamanio):
                print("Area de overflow llena.")
            else:
                self.__tabla[i][self.__conts[i]] = clave
                self.__conts[i] +=1
    # ====================

    # ===== Buscar =====
    def buscar(self, clave):
        claveHash = self.transformacion(clave)
        i = claveHash
        j = 0
        encontrado = False

        while not encontrado and j < self.__bucket:
            if(self.__tabla[i][j] == clave):
                encontrado = True
            else:
                j += 1
        if not encontrado:
            i = self.__areaOver
            j = 0
            while not encontrado and i < self.__tamanio:
                while j < self.__conts[i]:
                    if(self.__tabla[i][j] == clave):
                        encontrado = True
                    j += 1
                i += 1
                j = 0
            if(encontrado):
                print("Se encontro el elemento en el area de Overflow.")
            else:
                print("No se encontro el elemento")
        else: 
            print("Se encontro el elemento en el area primaria.")
    # ====================

    # ===== Recorrer tabla completa =====
    def recorrerHash(self):
        # Define cuántos caracteres de ancho tendrá cada "celda".
        # Si tus claves son muy largas (ej: 123456789), aumenta este número.
        ANCHO_CELDA = 4 
        
        print("--- INICIO TABLA HASH (Buckets) ---")
        print("\n=== ÁREA PRIMARIA ===")
        
        for i in range(self.__tamanio):
            if(i == self.__areaOver):
                print("\n=== ÁREA DE OVERFLOW ===")
            elementos_bucket = []
            for j in range(self.__bucket):
                valor_celda = self.__tabla[i][j]
                celda_formateada = f"{str(valor_celda):>{ANCHO_CELDA}}"
                elementos_bucket.append(celda_formateada)
            contenido = " | ".join(elementos_bucket)
            print(f"Bucket {i:02d}: [ {contenido} ]")
        print("--- FIN TABLA HASH ---")
    # ====================



    # ===== Muestra todos los valores con los que se crea la tabla =====
    def mostrarValores(self):
        print(f"""
            Valores:
            Tamanio: {self.__tamanio}
            Area Primaria: {self.__areaPrim}
            Overflow: {self.__areaOver}
            Bucket: {self.__bucket}
            """)
    # ====================