from prettytable import PrettyTable

from datos.auxiliares.validaciones import a_entero
from datos.repositorios.repo_receta_categorias import (
    actualizar_receta_categoria,
    agregar_receta_categoria,
    eliminar_receta_categoria,
    listar_receta_categorias,
)


def procesar_listado_receta_categorias(tabla: PrettyTable = None):
    if tabla is None:
        tabla = PrettyTable()
    tabla.field_names = ["ID Receta", "Receta", "ID Categoría", "Categoría"]
    tabla.clear_rows()
    for rc in listar_receta_categorias():
        tabla.add_row([rc.receta.id_receta, rc.receta.nombre, rc.categoria.id_categoria, rc.categoria.nombre])
    return tabla


def procesar_nueva_receta_categoria(id_receta, id_categoria):
    id_receta = a_entero(id_receta, "ID de la receta")
    id_categoria = a_entero(id_categoria, "ID de la categoría")
    if id_receta is None or id_categoria is None:
        return None
    nueva = agregar_receta_categoria(id_receta, id_categoria)
    if nueva:
        print("Categoría asignada a la receta exitosamente.")
    return nueva


def procesar_actualizacion_receta_categoria(id_receta, id_categoria_actual, id_categoria_nueva):
    id_receta = a_entero(id_receta, "ID de la receta")
    id_categoria_actual = a_entero(id_categoria_actual, "ID de la categoría actual")
    id_categoria_nueva = a_entero(id_categoria_nueva, "ID de la categoría nueva")
    if id_receta is None or id_categoria_actual is None or id_categoria_nueva is None:
        return False
    exito = actualizar_receta_categoria(id_receta, id_categoria_actual, id_categoria_nueva)
    if exito:
        print("Categoría de la receta actualizada exitosamente.")
    return exito


def procesar_eliminacion_receta_categoria(id_receta, id_categoria):
    id_receta = a_entero(id_receta, "ID de la receta")
    id_categoria = a_entero(id_categoria, "ID de la categoría")
    if id_receta is None or id_categoria is None:
        return False
    exito = eliminar_receta_categoria(id_receta, id_categoria)
    if exito:
        print("Categoría quitada de la receta exitosamente.")
    return exito
