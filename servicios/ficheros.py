import json
from datetime import date
from pathlib import Path
from servicios.biblioteca import Biblioteca
from modelos.libro import Libro
from modelos.usuario import Usuario
from modelos.prestamo import Prestamo

RUTA_DATOS = Path(__file__).resolve().parent.parent / "datos"

FICHERO_LIBROS= RUTA_DATOS / "libros.json"
FICHERO_USUARIOS= RUTA_DATOS / "usuarios.json"
FICHERO_PRESTAMOS= RUTA_DATOS /"prestamos.json"


def preparar_directorio():
        RUTA_DATOS.mkdir(exist_ok=True)



def guardar_biblioteca(biblioteca):
    guardar_json(
        FICHERO_LIBROS,
        [libro_a_dict(libro) for libro in biblioteca.libros]
    )
    guardar_json(
        FICHERO_USUARIOS,
        [usuario_a_dict(usuario) for usuario in biblioteca.usuarios]
    )
    guardar_json(
        FICHERO_PRESTAMOS,
        [to_dict(prestamo) for prestamo in biblioteca.prestamos]
    )


def guardar_json(fichero,datos):

    print(len(datos))

    with open(fichero,"w", encoding="utf-8") as f:
        json.dump(datos,f,ensure_ascii=False,indent=4)

def to_dict(prestamo):
    return {
        "usuario":prestamo.usuario.__dict__,
        "libro":prestamo.libro.__dict__,
        "fecha_prestamo":prestamo.fecha_prestamo.isoformat(),
        "activo":prestamo.activo,
        "fecha_devolucion":prestamo.fecha_devolucion.isoformat() if prestamo.fecha_devolucion is not None else None
    }

def libro_a_dict(libro):
    return {
                "isbn":libro.isbn,
                "titulo":libro.titulo,
                "autor":libro.autor,
                "genero":libro.genero,
                "anio":libro.anio,
                "disponible":libro.disponible
            }

def usuario_a_dict(usuario):
    return {
                "id":usuario.id,
                "nombre":usuario.nombre,
                "apellidos":usuario.apellidos,
                "email":usuario.email
            }

def cargar_datos(biblioteca):
     
     with open(FICHERO_LIBROS,"r", encoding="utf-8") as f:
        datos= json.load(f)

        for dato in datos:
            biblioteca.libros.append(Libro(**dato))
        
     with open(FICHERO_USUARIOS,"r", encoding="utf-8") as f:
        datos= json.load(f)
        for dato in datos:
            biblioteca.usuarios.append(Usuario(**dato))
    
     with open(FICHERO_PRESTAMOS,"r", encoding="utf-8") as f:
        datos= json.load(f)
        for dato in datos:
            usuario=Usuario(**dato["usuario"])
            libro=Libro(**dato["libro"])
            print(dato["fecha_devolucion"])
            biblioteca.prestamos.append(Prestamo(usuario,libro,date.fromisoformat(dato["fecha_prestamo"]),date.fromisoformat(dato["fecha_devolucion"] )if dato["fecha_devolucion"] is not None else None))
    
    