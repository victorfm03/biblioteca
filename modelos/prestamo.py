from datetime import date

class Prestamo:
    def __init__(self, usuario, libro, fecha_prestamo=None, fecha_devolucion=None):
        self.usuario = usuario
        self.libro = libro
        self.fecha_prestamo = (fecha_prestamo if fecha_prestamo is not None else date.today())
        self.fecha_devolucion = fecha_devolucion

    @property
    def activo(self):
        return self.fecha_devolucion is None
    

    def to_dict(self):
        return {
            "usuario":self.usuario.__dict__,
            "libro":self.libro.__dict__,
            "fecha_prestamo":self.fecha_prestamo.isoformat(),
            "activo":self.activo,
            "fecha_devolucion":self.fecha_devolucion.isoformat() if self.fecha_devolucion is not None else None
        }

    def __str__(self) -> str:
        return f"usuario: {self.usuario.nombre} {self.usuario.apellidos}\nLibro: {self.libro.titulo}\nfecha de prestamo: {self.fecha_prestamo}\nestado: {self.activo}"

