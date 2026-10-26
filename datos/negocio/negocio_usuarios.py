# CREATE TABLE usuario (
#     id_usuario      INT PRIMARY KEY AUTO_INCREMENT,
#     nombre          VARCHAR(100) NOT NULL,
#     email           VARCHAR(150) NOT NULL UNIQUE,
#     contrasena      VARCHAR(255) NOT NULL,
#     fecha_registro  DATE NOT NULL DEFAULT (CURRENT_DATE),
#     popularidad      INT NOT NULL DEFAULT 0
# );
from prettytable import PrettyTable
from datos.repositorios.repo_usuarios import listar_usuarios, agregar_usuario


def procesar_listado_usuarios(tabla: PrettyTable = None):
    if tabla is None:
        tabla = PrettyTable()
    tabla.field_names = ["ID", "Nombre", "email", "contrasena", "fecha_registro", "popularidad"]
    tabla.clear_rows()
    for u in listar_usuarios():
        tabla.add_row([u.id_usuario, u.nombre, u.email, u.contrasena, u.fecha_registro, u.popularidad])
    return tabla


def crear_usuario(nombre: str, email: str, contrasena: str):
    nuevo = agregar_usuario(nombre.strip(), email.strip(), contrasena)
    if nuevo:
        print(f"Usuario '{nuevo.nombre}' agregado exitosamente.")
    return nuevo
