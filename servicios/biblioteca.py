from modelos.libro import Libro
class Biblioteca:
    def __init__(self):
        self.usuarios = []
        self.prestamos = []
        self.libros= []

    def registrar_libro(self, libro_nuevo):
        #buscar si hay otro libro con el mismo isbn
        if self.buscar_libro(libro_nuevo):
            print("el libro ya esta en la lista")
            return
        self.libros.append(libro_nuevo)

    def buscar_libro(self, libro_nuevo):

        for libro in self.libros:
            #if libro.isbn == libro_nuevo.isbn:
            if libro.__eq__(libro_nuevo):

                return libro
        return None


    def registrar_usuario()