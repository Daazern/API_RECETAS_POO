from prettytable import PrettyTable

from datos.auxiliares.validaciones import a_entero
from datos.repositorios.repo_comentarios import (
    actualizar_comentario,
    agregar_comentario,
    eliminar_comentario,
    listar_comentarios,
)


def procesar_listado_comentarios(tabla: PrettyTable = None):
    if tabla is None:
        tabla = PrettyTable()
    tabla.field_names = ["ID", "Usuario", "Receta", "Comentario", "Fecha"]
    tabla.clear_rows()
    for c in listar_comentarios():
        tabla.add_row([c.id_comentario, c.usuario.nombre, c.receta.nombre, c.texto, c.fecha])
    return tabla


def procesar_nuevo_comentario(id_usuario, id_receta, texto: str):
    id_usuario = a_entero(id_usuario, "ID del usuario")
    id_receta = a_entero(id_receta, "ID de la receta")
    texto = texto.strip()
    if id_usuario is None or id_receta is None:
        return None
    if not texto:
        print("El comentario no puede estar vacío.")
        return None
    nuevo = agregar_comentario(id_usuario, id_receta, texto)
    if nuevo:
        print("Comentario agregado exitosamente.")
    return nuevo


def procesar_actualizacion_comentario(id_comentario, texto: str):
    id_comentario = a_entero(id_comentario, "ID del comentario")
    texto = texto.strip()
    if id_comentario is None:
        return None
    if not texto:
        print("El comentario no puede estar vacío.")
        return None
    comentario = actualizar_comentario(id_comentario, texto)
    if comentario:
        print(f"Comentario con ID {id_comentario} actualizado exitosamente.")
    return comentario


def procesar_eliminacion_comentario(id_comentario):
    id_comentario = a_entero(id_comentario, "ID del comentario")
    if id_comentario is None:
        return False
    exito = eliminar_comentario(id_comentario)
    if exito:
        print(f"Comentario con ID {id_comentario} eliminado exitosamente.")
    return exito
