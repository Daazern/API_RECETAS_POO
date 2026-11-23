from prettytable import PrettyTable

from datos.auxiliares.validaciones import a_entero
from datos.repositorios.repo_categorias import (
    actualizar_categoria,
    agregar_categoria,
    eliminar_categoria,
    listar_categorias,
)


def procesar_listado_categorias(tabla: PrettyTable = None):
    if tabla is None:
        tabla = PrettyTable()
    tabla.field_names = ["ID", "Nombre", "Tipo de comida"]
    tabla.clear_rows()
    for c in listar_categorias():
        tabla.add_row([c.id_categoria, c.nombre, c.tipo_comida])
    return tabla


def procesar_nueva_categoria(nombre: str, tipo_comida: str):
    nombre, tipo_comida = nombre.strip(), tipo_comida.strip()
    if not nombre or not tipo_comida:
        print("El nombre y el tipo de comida no pueden estar vacíos.")
        return None
    nueva = agregar_categoria(nombre, tipo_comida)
    if nueva:
        print(f"Categoría '{nueva.nombre}' agregada exitosamente.")
    return nueva


def procesar_actualizacion_categoria(id_categoria, nombre: str, tipo_comida: str):
    id_categoria = a_entero(id_categoria, "ID de la categoría")
    nombre, tipo_comida = nombre.strip(), tipo_comida.strip()
    if id_categoria is None:
        return None
    if not nombre or not tipo_comida:
        print("El nombre y el tipo de comida no pueden estar vacíos.")
        return None
    categoria = actualizar_categoria(id_categoria, nombre, tipo_comida)
    if categoria:
        print(f"Categoría con ID {id_categoria} actualizada exitosamente.")
    return categoria


def procesar_eliminacion_categoria(id_categoria):
    id_categoria = a_entero(id_categoria, "ID de la categoría")
    if id_categoria is None:
        return False
    exito = eliminar_categoria(id_categoria)
    if exito:
        print(f"Categoría con ID {id_categoria} eliminada exitosamente.")
    return exito
