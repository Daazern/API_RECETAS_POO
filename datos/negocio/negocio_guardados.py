from prettytable import PrettyTable

from datos.auxiliares.validaciones import a_entero
from datos.repositorios.repo_guardados import (
    actualizar_guardado,
    agregar_guardado,
    eliminar_guardado,
    listar_guardados,
)


def procesar_listado_guardados(tabla: PrettyTable = None):
    if tabla is None:
        tabla = PrettyTable()
    tabla.field_names = ["ID", "Usuario", "Receta", "Fecha guardado"]
    tabla.clear_rows()
    for g in listar_guardados():
        tabla.add_row([g.id_guardado, g.usuario.nombre, g.receta.nombre, g.fecha_guardado])
    return tabla


def procesar_nuevo_guardado(id_usuario, id_receta):
    id_usuario = a_entero(id_usuario, "ID del usuario")
    id_receta = a_entero(id_receta, "ID de la receta")
    if id_usuario is None or id_receta is None:
        return None
    nuevo = agregar_guardado(id_usuario, id_receta)
    if nuevo:
        print("Receta guardada exitosamente.")
    return nuevo


def procesar_actualizacion_guardado(id_guardado, id_usuario, id_receta):
    id_guardado = a_entero(id_guardado, "ID del guardado")
    id_usuario = a_entero(id_usuario, "ID del usuario")
    id_receta = a_entero(id_receta, "ID de la receta")
    if id_guardado is None or id_usuario is None or id_receta is None:
        return None
    guardado = actualizar_guardado(id_guardado, id_usuario, id_receta)
    if guardado:
        print(f"Guardado con ID {id_guardado} actualizado exitosamente.")
    return guardado


def procesar_eliminacion_guardado(id_guardado):
    id_guardado = a_entero(id_guardado, "ID del guardado")
    if id_guardado is None:
        return False
    exito = eliminar_guardado(id_guardado)
    if exito:
        print(f"Guardado con ID {id_guardado} eliminado exitosamente.")
    return exito
