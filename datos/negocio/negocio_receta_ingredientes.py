from prettytable import PrettyTable

from datos.auxiliares.validaciones import a_decimal, a_entero
from datos.repositorios.repo_receta_ingredientes import (
    actualizar_receta_ingrediente,
    agregar_receta_ingrediente,
    eliminar_receta_ingrediente,
    listar_receta_ingredientes,
)


def _validar_cantidad(cantidad):
    valor = a_decimal(cantidad, "cantidad")
    if valor is None:
        return None
    if valor <= 0:
        print("La cantidad debe ser mayor a 0.")
        return None
    return valor


def procesar_listado_receta_ingredientes(tabla: PrettyTable = None):
    if tabla is None:
        tabla = PrettyTable()
    tabla.field_names = ["ID Receta", "Receta", "ID Ingrediente", "Ingrediente", "Cantidad", "Unidad"]
    tabla.clear_rows()
    for ri in listar_receta_ingredientes():
        tabla.add_row([
            ri.receta.id_receta, ri.receta.nombre,
            ri.ingrediente.id_ingrediente, ri.ingrediente.nombre,
            ri.cantidad, ri.ingrediente.unidad_medida,
        ])
    return tabla


def procesar_nuevo_receta_ingrediente(id_receta, id_ingrediente, cantidad):
    id_receta = a_entero(id_receta, "ID de la receta")
    id_ingrediente = a_entero(id_ingrediente, "ID del ingrediente")
    cantidad = _validar_cantidad(cantidad)
    if id_receta is None or id_ingrediente is None or cantidad is None:
        return None
    nuevo = agregar_receta_ingrediente(id_receta, id_ingrediente, cantidad)
    if nuevo:
        print("Ingrediente asignado a la receta exitosamente.")
    return nuevo


def procesar_actualizacion_receta_ingrediente(id_receta, id_ingrediente, cantidad):
    id_receta = a_entero(id_receta, "ID de la receta")
    id_ingrediente = a_entero(id_ingrediente, "ID del ingrediente")
    cantidad = _validar_cantidad(cantidad)
    if id_receta is None or id_ingrediente is None or cantidad is None:
        return False
    exito = actualizar_receta_ingrediente(id_receta, id_ingrediente, cantidad)
    if exito:
        print("Cantidad actualizada exitosamente.")
    return exito


def procesar_eliminacion_receta_ingrediente(id_receta, id_ingrediente):
    id_receta = a_entero(id_receta, "ID de la receta")
    id_ingrediente = a_entero(id_ingrediente, "ID del ingrediente")
    if id_receta is None or id_ingrediente is None:
        return False
    exito = eliminar_receta_ingrediente(id_receta, id_ingrediente)
    if exito:
        print("Ingrediente quitado de la receta exitosamente.")
    return exito
