from prettytable import PrettyTable

from datos.auxiliares.validaciones import a_entero
from datos.repositorios.repo_valoraciones import (
    actualizar_valoracion,
    agregar_valoracion,
    eliminar_valoracion,
    listar_valoraciones,
)


def _validar_puntuacion(puntuacion):
    valor = a_entero(puntuacion, "puntuación")
    if valor is None:
        return None
    if not 1 <= valor <= 5:
        print("La puntuación debe estar entre 1 y 5.")
        return None
    return valor


def procesar_listado_valoraciones(tabla: PrettyTable = None):
    if tabla is None:
        tabla = PrettyTable()
    tabla.field_names = ["ID", "Usuario", "Receta", "Puntuación", "Fecha"]
    tabla.clear_rows()
    for v in listar_valoraciones():
        tabla.add_row([v.id_valoracion, v.usuario.nombre, v.receta.nombre, v.puntuacion, v.fecha])
    return tabla


def procesar_nueva_valoracion(id_usuario, id_receta, puntuacion):
    id_usuario = a_entero(id_usuario, "ID del usuario")
    id_receta = a_entero(id_receta, "ID de la receta")
    puntuacion = _validar_puntuacion(puntuacion)
    if id_usuario is None or id_receta is None or puntuacion is None:
        return None
    nueva = agregar_valoracion(id_usuario, id_receta, puntuacion)
    if nueva:
        print("Valoración agregada exitosamente.")
    return nueva


def procesar_actualizacion_valoracion(id_valoracion, puntuacion):
    id_valoracion = a_entero(id_valoracion, "ID de la valoración")
    puntuacion = _validar_puntuacion(puntuacion)
    if id_valoracion is None or puntuacion is None:
        return None
    valoracion = actualizar_valoracion(id_valoracion, puntuacion)
    if valoracion:
        print(f"Valoración con ID {id_valoracion} actualizada exitosamente.")
    return valoracion


def procesar_eliminacion_valoracion(id_valoracion):
    id_valoracion = a_entero(id_valoracion, "ID de la valoración")
    if id_valoracion is None:
        return False
    exito = eliminar_valoracion(id_valoracion)
    if exito:
        print(f"Valoración con ID {id_valoracion} eliminada exitosamente.")
    return exito
