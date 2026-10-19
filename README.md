# biblioteca

## Descripción

Aplicación de consola en Python para la gestión de una biblioteca. Permite registrar libros y usuarios, buscar y listar libros, gestionar préstamos y devoluciones, y persistir toda la información en ficheros JSON.

## Instalación

No requiere dependencias externas; solo Python 3.

1. Clona o descarga el proyecto.
2. Asegúrate de tener Python 3 instalado:

```bash
python --version
```

## Ejecución

Ejecuta el programa **desde la raíz del proyecto**, ya que los ficheros de datos se cargan con rutas relativas a la carpeta `datos/`:

```bash
python main.py
```

Al arrancar verás un menú con las opciones disponibles.

## Estructura del proyecto

```text
biblioteca/
├── main.py                 # Punto de entrada y menú de consola
├── README.md
├── datos/                  # Persistencia en JSON
│   ├── libros.json
│   ├── usuarios.json
│   └── prestamos.json
├── modelos/                # Entidades del dominio
│   ├── libro.py
│   ├── usuario.py
│   └── prestamo.py
└── servicios/
    └── biblioteca.py       # Lógica de gestión y carga/guardado de datos
```

## Clases utilizadas

### Libro (`modelos/libro.py`)

| Atributo | Descripción |
| --- | --- |
| `isbn` | Identificador del libro |
| `titulo` | Título |
| `autor` | Autor |
| `anio` | Año de publicación |
| `genero` | Género |
| `disponible` | Indica si está disponible para préstamo |

- `__eq__`: dos libros son iguales si tienen el mismo `isbn`.
- `isDisponible`: propiedad que devuelve "Disponible" o "Prestado".

### Usuario (`modelos/usuario.py`)

| Atributo | Descripción |
| --- | --- |
| `id` | Identificador del usuario |
| `nombre` | Nombre |
| `apellidos` | Apellidos |
| `email` | Correo electrónico |

- `__eq__`: dos usuarios son iguales si tienen el mismo `id`.

### Prestamo (`modelos/prestamo.py`)

| Atributo | Descripción |
| --- | --- |
| `usuario` | Usuario que realiza el préstamo |
| `libro` | Libro prestado |
| `fecha_prestamo` | Fecha del préstamo (por defecto, hoy) |
| `fecha_devolucion` | Fecha de devolución (vacía mientras está activo) |

- `activo`: propiedad que indica si el préstamo sigue activo (sin fecha de devolución).
- `to_dict()`: serializa el préstamo a un diccionario para guardarlo en JSON.

### Biblioteca (`servicios/biblioteca.py`)

Clase principal que coordina todo: mantiene las listas de libros, usuarios y préstamos, y se encarga de cargar y guardar los datos en la carpeta `datos/`.

- `registrar_libro` / `registrar_usuario`: alta evitando duplicados.
- `buscar_libro_por_isbn` / `buscar_usuario_por_id`: búsquedas por identificador.
- `registrarPrestamo`: valida disponibilidad y registra el préstamo.
- `mostrar_prestamos_activos` / `prestamo_por_usuario`: consultas de préstamos.
- `cargar_datos` / `guardar_datos`: persistencia en JSON.

## Funcionalidades disponibles

| Opción | Acción |
| --- | --- |
| 1 | Registrar libro |
| 2 | Registrar usuario |
| 3 | Buscar libro (por ISBN, título o autor) |
| 4 | Listar libros |
| 5 | Realizar préstamo |
| 6 | Registrar devolución |
| 7 | Mostrar préstamos activos |
| 8 | Mostrar préstamos de un usuario |
| 9 | Guardar datos |
| 0 | Salir |
