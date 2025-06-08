class Libro:
    __titulo: str
    __autor: str
    __isbn: str
    __genero: str
    def __init__(self, titulo = "", autor = "", isbn = "", genero = ""):
        self.__titulo = titulo
        self.__autor = autor
        self.__isbn = isbn
        self.__genero = genero
    def obtTitulo(self):
        return self.__titulo
    def obtAutor(self):
        return self.__autor
    def obtIsbn(self):
        return self.__isbn
    def obtGenero(self):
        return self.__genero