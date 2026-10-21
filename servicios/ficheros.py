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

    libros=[libro.__dict__ for libro in biblioteca.libros]

    guardar_json(FICHERO_LIBROS,libros)

    usuarios=[usuario.usuario_a_dict() for usuario in biblioteca.usuarios]

    guardar_json(FICHERO_USUARIOS,usuarios)

    prestamos=[prestamo.to_dict() for prestamo in biblioteca.prestamos]

    guardar_json(FICHERO_PRESTAMOS, prestamos)

def guardar_json(fichero,datos):

    print(len(datos))

    with open(fichero,"w", encoding="utf-8") as f:
        json.dump(datos,f,ensure_ascii=False,indent=4)



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
            
            if usuario is None or libro is None:
                return
            
            biblioteca.prestamos.append(Prestamo(usuario,libro,date.fromisoformat(dato["fecha_prestamo"]),date.fromisoformat(dato["fecha_devolucion"] )if dato["fecha_devolucion"] is not None else None))
