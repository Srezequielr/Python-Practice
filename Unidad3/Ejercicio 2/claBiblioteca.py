class Biblioteca:
    __nombre: str
    __direccion: str
    __telefono: str
    __libros: list
    def __init__(self, nombre, direccion, telefono):
        self.__nombre = nombre
        self.__direccion = direccion
        self.__telefono = telefono
        self.__libros = []
    def obtNombre(self):
        return self.__nombre
    def obtDireccion(self):
        return self.__direccion
    def obtTelefono(self):
        return self.__telefono
    def obtLibros(self):
        return self.__libros
    def agregarLibro(self, libro):
        self.__libros.append(libro)
        return 1
    def aliminarLibro(self, titulo):
        indice
        i = 0
        encontrado = False
        cantidad = len(self.__libros)
        while i < cantidad and not encontrado:
            if titulo == self.__libros[i]:
                encontrado = True
                indice = i
            i += 1
        if encontrado:
            self.__libros.pop(indice)
            print("Libro eliminado correctamente")
        else: 
            print("Libro no encontrado")