from prettytable import PrettyTable

from datos.repositorios.repo_ingredientes import (
    actualizar_ingrediente,
    agregar_ingrediente,
    eliminar_ingrediente,
    listar_ingredientes,
)


def procesar_listado_ingredientes(tabla: PrettyTable):
    if tabla:
        tabla.field_names = ["ID", "Nombre", "Unidad de Medida"]
        tabla.clear_rows()
        for ingrediente in listar_ingredientes():
            tabla.add_row([ingrediente.id_ingrediente, ingrediente.nombre, ingrediente.unidad_medida])
        return tabla


def procesar_nuevo_ingrediente(nombre: str, unidad_medida: str):    
    return agregar_ingrediente(nombre.strip(), unidad_medida.strip())


def procesar_actualizacion_ingrediente(id_ingrediente: int, nombre: str, unidad_medida: str):
    return actualizar_ingrediente(id_ingrediente, nombre.strip(), unidad_medida.strip())

def procesar_eliminacion_ingrediente(id_ingrediente: int):
    return eliminar_ingrediente(id_ingrediente)