from prettytable import PrettyTable

from datos.auxiliares.validaciones import a_entero
from datos.repositorios.repo_recetas import (
    actualizar_receta,
    agregar_receta,
    eliminar_receta,
    listar_recetas,
    obtener_receta_por_id,
)

DIFICULTADES = ("facil", "media", "dificil")


def _validar_datos_receta(nombre, tiempo_preparacion, dificultad, instrucciones):
    """Retorna (tiempo, dificultad) ya validados o None si hay algún error."""
    if not nombre or not instrucciones:
        print("El nombre y las instrucciones no pueden estar vacíos.")
        return None
    tiempo = a_entero(tiempo_preparacion, "tiempo de preparación (minutos)")
    if tiempo is None:
        return None
    if tiempo <= 0:
        print("El tiempo de preparación debe ser mayor a 0.")
        return None
    dificultad = dificultad.strip().lower()
    if dificultad not in DIFICULTADES:
        print(f"La dificultad debe ser una de: {', '.join(DIFICULTADES)}.")
        return None
    return tiempo, dificultad


def procesar_listado_recetas(tabla: PrettyTable = None):
    if tabla is None:
        tabla = PrettyTable()
    tabla.field_names = ["ID", "Autor", "Nombre", "Tiempo (min)", "Dificultad", "Publicada"]
    tabla.clear_rows()
    for r in listar_recetas():
        tabla.add_row([r.id_receta, r.usuario.nombre, r.nombre, r.tiempo_preparacion, r.dificultad, r.fecha_publicacion])
    return tabla


def procesar_detalle_receta(id_receta):
    id_receta = a_entero(id_receta, "ID de la receta")
    if id_receta is None:
        return None
    r = obtener_receta_por_id(id_receta)
    if not r:
        return None
    return (
        f"\n{r.nombre} (por {r.usuario.nombre})\n"
        f"Tiempo: {r.tiempo_preparacion} min | Dificultad: {r.dificultad} | Publicada: {r.fecha_publicacion}\n"
        f"Descripción: {r.descripcion or '(sin descripción)'}\n"
        f"Instrucciones:\n{r.instrucciones}"
    )


def procesar_nueva_receta(id_usuario, nombre: str, descripcion: str, tiempo_preparacion, dificultad: str, instrucciones: str):
    id_usuario = a_entero(id_usuario, "ID del usuario")
    nombre, descripcion, instrucciones = nombre.strip(), descripcion.strip(), instrucciones.strip()
    if id_usuario is None:
        return None
    validados = _validar_datos_receta(nombre, tiempo_preparacion, dificultad, instrucciones)
    if validados is None:
        return None
    tiempo, dificultad = validados
    nueva = agregar_receta(id_usuario, nombre, descripcion or None, tiempo, dificultad, instrucciones)
    if nueva:
        print(f"Receta '{nueva.nombre}' agregada exitosamente.")
    return nueva


def procesar_actualizacion_receta(id_receta, nombre: str, descripcion: str, tiempo_preparacion, dificultad: str, instrucciones: str):
    id_receta = a_entero(id_receta, "ID de la receta")
    nombre, descripcion, instrucciones = nombre.strip(), descripcion.strip(), instrucciones.strip()
    if id_receta is None:
        return None
    validados = _validar_datos_receta(nombre, tiempo_preparacion, dificultad, instrucciones)
    if validados is None:
        return None
    tiempo, dificultad = validados
    receta = actualizar_receta(id_receta, nombre, descripcion or None, tiempo, dificultad, instrucciones)
    if receta:
        print(f"Receta con ID {id_receta} actualizada exitosamente.")
    return receta


def procesar_eliminacion_receta(id_receta):
    id_receta = a_entero(id_receta, "ID de la receta")
    if id_receta is None:
        return False
    exito = eliminar_receta(id_receta)
    if exito:
        print(f"Receta con ID {id_receta} eliminada exitosamente.")
    return exito
