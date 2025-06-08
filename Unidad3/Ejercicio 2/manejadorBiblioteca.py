import csv
from claBiblioteca import Biblioteca
from claLibro import Libro

class ManejadorBiblioteca:
    __bibliotecas: list
    __libros: list
    def __init__(self):
        self.__bibliotecas = []
        self.__libros = []
    def cargarCSV(self):
        archivo = open("Biblioteca.csv", "r", encoding="UTF-8")
        reader = csv.reader(archivo, delimiter=";")
        for fila in reader:
            if len(fila) == 3:
                #Es una biblioteca
                biblioteca = Biblioteca(fila[0], fila[1], fila[2])
                self.__bibliotecas.append(biblioteca)
            if len(fila) == 4:
                #Es un libro   
                libro = Libro(fila[0], fila[1], fila[2], fila[4])
                biblioteca.agregarLibro(libro)
                self.__libros.append()
    def buscarBiblioteca(self):
        nomBiblio = input("Ingrese nombre de la biblioteca: ")
        encontrado = bool
        resultado = False
        i = 0
        cantidad = len(self.__bibliotecas)
        while not encontrado and i < cantidad:
            if nomBiblio == self.__bibliotecas[i].obtNombre():
                encontrado = True
                resultado = self.__bibliotecas[i] 
            i += 1
        return resultado       
    def agregarLibro(self):
        biblioteca = self.buscarBiblioteca()
        if not biblioteca:
            print("Biblioteca no encontrada")
            return 
        titulo = input("Ingrese nombre de libro: ")
        autor = input("Ingrese autor: ")
        isbn = input("Ingrese isbn: " )
        genero = input("Ingrese genero: ")
        libro = Libro(titulo, autor, isbn, genero)
        self.__libros.append(libro)
        biblioteca.agregarLibro(libro)
    def eliminarLibro(self):
        biblioteca = self.buscarBiblioteca()
        
        if not biblioteca:
            print("Biblioteca no encontrada")
            return
        titulo = input("Ingrese nombre del libro a eliminar: ")
        biblioteca.aliminarLibro(titulo)
        