import numpy as np

class Grafo:
    __cant: int
    __matAdy: np.array
    def __init__(self, cant = 5):
        self.__cant = cant
        self.__matAdy = np.zeros((cant, cant), dtype=int)
    
    # ===== Crear Arista =====
    def crearArista(self, origen, destino):
        if(origen > self.__cant or destino > self.__cant):
            print("Conexion invalida.")
        else:
            self.__matAdy[origen - 1, destino - 1] = 1
    # ====================

    # ===== Adyasencia =====
    def adyacente(self, vertice):
        if(self.__cant < vertice):
            print("Vertice invalido")
        else:
            for i in range(self.__cant):
                if(self.__matAdy[vertice -1 ][i] == 1):
                    print(i + 1)
    # ====================

    # ===== Muestra el grado de salida de un nodo =====
    def gradoSalida(self, vertice):
        grado = 0
        if(self.__cant < vertice):
            print("Vertice invalido")
        else:
            for i in range(self.__cant):
                if(self.__matAdy[vertice -1 ][i] == 1):
                    grado += 1
        return grado
    # ====================

    # ===== Muestra grado de entrada de un nodo =====
    def gradoEntrada(self, vertice):
        grado = 0
        if(self.__cant < vertice):
            print("Vertice invalido")
        else:
            for i in range(self.__cant):
                if(self.__matAdy[i][vertice - 1] == 1):
                    grado += 1
        return grado
    # ====================

    # ===== Verifica si un vertice es fuente =====
    def nodoF(self, vertice):
        if(self.gradoEntrada(vertice) == 0 and self.gradoSalida(vertice) > 0):
            return True
        else:
            return False
    # ====================

    # ===== Verifica si un vertice es sumidero =====
    def nodoS(self, vertice):
        if(self.gradoEntrada(vertice) > 0 and self.gradoSalida(vertice) == 0):
            return True
        else: 
            return False
    # ====================

    # ===== Mostrar Matriz adyasencia =====
    def recorrerMatAdy(self):
        print(self.__matAdy)
    # ====================

    # ===== Mostrar camino entre un vertice A y B 
    def camino(self, a, b):
        pass
    # ====================
