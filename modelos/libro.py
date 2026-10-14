class Libro:
    def __init__(self, isbn, titulo, autor, genero, anio=None, disponible=True):
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.anio = anio
        self.genero = genero
        self.disponible = disponible

    def __str__(self) -> str:
        return f"Código: {self.isbn}\nTítulo: {self.titulo}\nAutor: {self.autor}\nAño: {self.anio}\nGénero: {self.genero}\nEstado: {self.isDisponible}"

    @property
    def isDisponible(self)-> bool:
        estado = "Disponible" if self.disponible else "Prestado"
        return estado
    
    def __eq__(self,valor):
        return self.isbn ==valor.isbn