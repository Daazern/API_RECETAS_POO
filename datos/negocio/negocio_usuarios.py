# CREATE TABLE usuario (
#     id_usuario      INT PRIMARY KEY AUTO_INCREMENT,
#     nombre          VARCHAR(100) NOT NULL,
#     email           VARCHAR(150) NOT NULL UNIQUE,
#     contrasena      VARCHAR(255) NOT NULL,
#     fecha_registro  DATE NOT NULL DEFAULT (CURRENT_DATE),
#     popularidad      INT NOT NULL DEFAULT 0
# );
# alter table usuario add column rut varchar(12) not null unique;
from prettytable import PrettyTable
from datos.auxiliares.validaciones import (
    a_entero,
    encriptar_contrasena,
    validar_formato_contrasena,
    validar_formato_email,
    validar_rut,
    verificar_contrasena,
)
from datos.repositorios.repo_usuarios import buscar_usuario_por_email, listar_usuarios, agregar_usuario, actualizar_usuario, eliminar_usuario, obtener_usuario_por_id


def procesar_listado_usuarios(tabla: PrettyTable = None):
    if tabla is None:
        tabla = PrettyTable()
    tabla.field_names = ["ID", "Nombre", "email", "RUT", "fecha_registro", "popularidad"]
    tabla.clear_rows()
    for u in listar_usuarios():
        tabla.add_row([u.id_usuario, u.nombre, u.email, u.rut, u.fecha_registro, u.popularidad])
    return tabla


def crear_usuario(nombre: str, email: str, contrasena: str, rut: str):
    nombre = nombre.strip()
    if not nombre:
        print("El nombre no puede estar vacío.")
        return None
    email = validar_formato_email(email)
    rut = validar_rut(rut)
    if email is None or rut is None or not validar_formato_contrasena(contrasena):
        return None
    nuevo = agregar_usuario(nombre, email, encriptar_contrasena(contrasena), rut)
    if nuevo:
        print(f"Usuario '{nuevo.nombre}' agregado exitosamente.")
    return nuevo


def actualizar_usuario_existente(id_usuario, nombre: str, email: str, contrasena: str, rut: str):
    """Si contrasena viene vacía se conserva la contraseña (hash) actual."""
    id_usuario = a_entero(id_usuario, "ID del usuario")
    if id_usuario is None:
        return None
    nombre = nombre.strip()
    if not nombre:
        print("El nombre no puede estar vacío.")
        return None
    email = validar_formato_email(email)
    rut = validar_rut(rut)
    if email is None or rut is None:
        return None
    if contrasena:
        if not validar_formato_contrasena(contrasena):
            return None
        hash_contrasena = encriptar_contrasena(contrasena)
    else:
        actual = obtener_usuario_por_id(id_usuario)
        if not actual:
            return None
        hash_contrasena = actual["contrasena"]
    usuario_actualizado = actualizar_usuario(id_usuario, nombre, email, hash_contrasena, rut)
    if usuario_actualizado:
        print(f"Usuario con ID {id_usuario} actualizado exitosamente.")
    return usuario_actualizado


def eliminar_usuario_existente(id_usuario: int):
    id_usuario = a_entero(id_usuario, "ID del usuario")
    if id_usuario is None:
        return False
    exito = eliminar_usuario(id_usuario)
    if exito:
        print(f"Usuario con ID {id_usuario} eliminado exitosamente.")
    return exito


_hash_falso = None


def autenticar_usuario(email: str, contrasena: str):
    """Retorna el usuario si las credenciales son correctas; si no, None.
    El mensaje es el mismo para email inexistente o contraseña errónea."""
    global _hash_falso
    usuario = buscar_usuario_por_email((email or "").strip())
    if usuario is None:
        # se compara contra un hash falso para no revelar por tiempo si el email existe
        if _hash_falso is None:
            _hash_falso = encriptar_contrasena("contrasena-falsa")
        verificar_contrasena(contrasena or "", _hash_falso)
        print("Email o contraseña incorrectos.")
        return None
    if not verificar_contrasena(contrasena or "", usuario.contrasena):
        print("Email o contraseña incorrectos.")
        return None
    return usuario
