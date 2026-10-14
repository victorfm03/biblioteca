from modelos.libro import Libro
from modelos.usuario import Usuario
from modelos.prestamo import Prestamo


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


    def registrar_usuario(self, usuario_nuevo):
        #buscar si hay otro usuario con el mismo id
        if self.buscar_usuario(usuario_nuevo):
            print("el usuario ya esta en la lista")
            return
        self.usuarios.append(usuario_nuevo)
    
    def buscar_usuario(self,usuario_nuevo):
        for usuario in self.usuarios:
            #if usuario.id == usuario_nuevo.id:
            if usuario.__eq__(usuario_nuevo):

                return usuario
        return None
        
    def registrarPrestamo(self,nuevo_prestamo):
        #buscar el libro
        libro=self.buscar_libro(nuevo_prestamo.libro)
        if libro is None:
            print("No existe ese libro")
            return
        #comprobar si esta disponible
        if not libro.disponible:
            print("el libro no esta disponible")
            return
        
        self.prestamos.append(nuevo_prestamo)

        #cambiar el estado del libro
        libro.disponible=False

        for prestamo in self.prestamos:
            if prestamo== nuevo_prestamo:
                print(prestamo)
        print("Préstamo realizado correctamente.")


    def buscar_libro_por_isbn(self, isbn):
        for libro in self.libros:
            if libro.isbn == isbn:
                return libro
        return None

    def buscar_usuario_por_id(self, id_usuario):
        for usuario in self.usuarios:
            if usuario.id == id_usuario:
                return usuario
        return None