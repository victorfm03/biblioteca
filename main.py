from modelos.libro import Libro
from modelos.prestamo import Prestamo
from modelos.usuario import Usuario
from servicios.biblioteca import Biblioteca
from datetime import date

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

def buscar_libro(biblioteca):
    print("1. Buscar por ISBN")
    print("2. Buscar por Titulo")
    print("3. Buscar por Autor")
    
    buscar=input("elige el criterio de busqueda: ")


    libroBuscado=None
    if buscar=="1" or buscar=="2" or buscar=="3":
        valor=input("Di el libro a buscar: ")
        """for libro in biblioteca.libros:
            if buscar=="1" and libro.isbn==valor:
                libroBuscado=libro
            elif buscar=="2" and libro.titulo==valor:
                libroBuscado=libro
            elif buscar=="3" and libro.autor==valor:
                libroBuscado=libro"""

        libroBuscado=[libro.__str__() for libro in biblioteca.libros if buscar =="1" and libro.isbn==valor or buscar=="2" and libro.titulo==valor or buscar=="3" and libro.autor==valor]
        libroBuscado=libroBuscado[0]
    else:
        print("opcion no valida")

    return libroBuscado


def listar_libros(biblioteca):
    for libro in biblioteca.libros:
        print(f"{libro}\n")

def realizar_prestamo(biblioteca):
    
    idUsuario= int(input("id del usuario que hara el prestamo: "))
    isbnLibro= input("di el isbn del prestamo: ")

    usuario=biblioteca.buscar_usuario_por_id(idUsuario)
    libro= biblioteca.buscar_libro_por_isbn(isbnLibro)

    prestamo=Prestamo(usuario,libro)
    biblioteca.registrarPrestamo(prestamo)
    
def registrarDevolucion(biblioteca):
    isbnLibro= input("di el isbn del libro a devolver: ")
    libro= biblioteca.buscar_libro_por_isbn(isbnLibro)

    if libro is None:
        print("No existe ese libro")
        return

    if libro.disponible:
        print("Ese libro ya está disponible")
        return
    
    for prestamo in biblioteca.prestamos:
        if prestamo.libro== libro and prestamo.activo:
            prestamo.fecha_devolucion=date.today()
    
    libro.disponible=True
    print(f"Código del libro: {libro.isbn}")
    print("Libro devuelto correctamente.")

def mostrar_prestamos(biblioteca):
    biblioteca.mostrar_prestamos_activos()

def prestamos_de_usuario(biblioteca):
    idUsuario=int(input("Di el id de usuario para ver sus prestamos: "))
    biblioteca.prestamo_por_usuario(idUsuario)

def guardar_datos(biblioteca):
    biblioteca.guardar_datos()
    
def main():

    biblioteca = Biblioteca()

    while True:
        menu()
        opcion = input("Opcion: ")
        if opcion == "1":
            registrar_libro(biblioteca)
        elif opcion == "2":
            registrar_usuario(biblioteca)
        elif opcion == "3":
            print(buscar_libro(biblioteca))
        elif opcion == "4":
            listar_libros(biblioteca)
        elif opcion == "5":
            realizar_prestamo(biblioteca)
        elif opcion == "6":
            registrarDevolucion(biblioteca)
        elif opcion == "7":
            mostrar_prestamos(biblioteca)
        elif opcion == "8":
            prestamos_de_usuario(biblioteca)
        elif opcion =="9":
            guardar_datos(biblioteca)
        elif opcion == "0":
            return

if __name__ == "__main__":
    main()