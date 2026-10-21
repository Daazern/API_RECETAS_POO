from prettytable import PrettyTable

from datos.repositorios.repo_ingredientes import agregar_ingrediente, listar_ingredientes


def procesar_listado_ingredientes(tabla: PrettyTable) -> PrettyTable:
    tabla.field_names = ["ID", "Nombre", "Unidad de Medida"]
    tabla.clear_rows()
    for ingrediente in listar_ingredientes():
        tabla.add_row([ingrediente.id_ingrediente, ingrediente.nombre, ingrediente.unidad_medida])
    return tabla


def procesar_nuevo_ingrediente(nombre: str, unidad_medida: str):
    return agregar_ingrediente(nombre, unidad_medida)


def procesar_actualizacion_ingrediente(id_ingrediente: int, nombre: str, unidad_medida: str):
    # Aquí puedes implementar la lógica para actualizar un ingrediente
    pass

def procesar_eliminacion_ingrediente(id_ingrediente: int):
    # Aquí puedes implementar la lógica para eliminar un ingrediente
    pass
