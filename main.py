from modelos.libro import Libro
from modelos.prestamo import Prestamo
from modelos.usuario import Usuario
from servicios.biblioteca import Biblioteca

def menu():
    print()
    print("=================================")
    print(" GESTIÓN DE BIBLIOTECA")
    print("=================================")
    print("""
        1. Registrar libro\n
        2. Registrar usuario\n
        3. Buscar libro\n
        4. Listar libros\n
        5. Realizar préstamo\n
        6. Registrar devolución\n
        7. Mostrar préstamos activos\n
        8. Mostrar préstamos de un usuario\n
        9. Guardar datos\n
        0. Salir
        """)
    print("=================================")

def registrar_libro(biblioteca):
    isbn = input('ISBN: ').strip()
    titulo= input('Titulo: ').strip()
    autor= input('Autor: ').strip()
    anio= input('Año: ').strip()
    genero= input('Genero: ').strip()

    libro= Libro(isbn,titulo,autor,anio,genero)
    biblioteca.registrar_libro(libro)

def registrar_usuario(biblioteca):
    id = int(input("id: ").strip())
    nombre = input("nombre: ").strip()
    apellidos = input("apellidos: ").strip()
    email = input("email: ").strip()

    usuario= Usuario(id,nombre,apellidos,email)
    biblioteca.registrar_usuario(usuario)

def main():

    biblioteca = Biblioteca()

    while True:
        menu()
        opcion = input("Opcion: ")
        if opcion == "1":
            registrar_libro(biblioteca)
        elif opcion == "2":
            pass
        elif opcion == "3":
            pass
        elif opcion == "4":
            pass
        elif opcion == "5":
            pass
        elif opcion == "6":
            pass
        elif opcion == "7":
            pass
        elif opcion == "8":
            pass
        elif opcion == "0":
            pass

if __name__ == "__main__":
    main()