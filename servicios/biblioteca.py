import json
from datetime import date
from pathlib import Path
from modelos.libro import Libro
from modelos.usuario import Usuario
from modelos.prestamo import Prestamo


class Biblioteca:
    RUTA_DATOS = Path("datos")

    def __init__(self):
        self.usuarios = []
        self.prestamos = []
        self.libros= []
        #self.cargar_datos()

    def registrar_libro(self, libro_nuevo):
        #buscar si hay otro libro con el mismo isbn
        if self.buscar_libro(libro_nuevo):
            raise ValueError("el libro ya esta en la lista")
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
            raise ValueError("el usuario ya esta en la lista")
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
            raise ValueError("No existe ese libro")
        #comprobar si esta disponible
        if not libro.disponible:
            raise ValueError("el libro no esta disponible")
        
        self.prestamos.append(nuevo_prestamo)

        #cambiar el estado del libro
        libro.prestar()

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
    
    def mostrar_prestamos_activos(self):
        encontrado=False
        for prestamo in self.prestamos:
            if prestamo.activo:
                print(prestamo)
                encontrado=True
        
        if not encontrado:
            print("No hay prestamos activos")

    def prestamo_por_usuario(self, id_usuario):
        usuario=self.buscar_usuario_por_id(id_usuario)
        if usuario is None:
            print("No existe el usuario")
            return
        
        encontrado=False

        for prestamo in self.prestamos:
            if prestamo.usuario == usuario:
                print(prestamo)
                encontrado=True
                
        if not encontrado:
            print("El usuario no tiene prestamos activos")

    """def guardar_datos(self):
        with open(self.RUTA_DATOS / "libros.json", "w", encoding="utf-8") as fichero:
            json.dump([libro.__dict__ for libro in self.libros], fichero, ensure_ascii=False, indent=4)

        with open(self.RUTA_DATOS / "usuarios.json", "w", encoding="utf-8") as fichero:
            json.dump([usuario.__dict__ for usuario in self.usuarios], fichero, ensure_ascii=False, indent=4)
        
        with open(self.RUTA_DATOS / "prestamos.json", "w", encoding="utf-8") as fichero:
            json.dump([prestamo.to_dict() for prestamo in self.prestamos], fichero, ensure_ascii=False, indent=4)

    def cargar_datos(self):
        if (self.RUTA_DATOS / "libros.json").exists():
            with open(self.RUTA_DATOS / "libros.json", encoding="utf-8") as fichero:
                self.libros= [Libro(**datos) for datos in json.load(fichero)]

        if (self.RUTA_DATOS / "usuarios.json").exists():
            with open(self.RUTA_DATOS / "usuarios.json", encoding="utf-8") as fichero:
                self.usuarios= [Usuario(**datos) for datos in json.load(fichero)]

        if (self.RUTA_DATOS / "prestamos.json").exists():
            with open(self.RUTA_DATOS / "prestamos.json", encoding="utf-8") as fichero:
                self.prestamos= [self._prestamo_desde_dict(datos) for datos in json.load(fichero)]"""

    def _prestamo_desde_dict(self, datos):
        usuario= Usuario(**datos["usuario"])
        libro= Libro(**datos["libro"])
        fecha_prestamo= date.fromisoformat(datos["fecha_prestamo"])
        fecha_devolucion= date.fromisoformat(datos["fecha_devolucion"]) if datos["fecha_devolucion"] else None
        return Prestamo(usuario, libro, fecha_prestamo, fecha_devolucion)
