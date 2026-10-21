from prettytable import PrettyTable 

from datos.repositorios.repo_ingredientes import listar_ingredientes

def listado_ingredientes(tabla:PrettyTable):
    if tabla:
        tabla.field_names = ["ID", "Nombre", "Unidad de Medida"]
        listado_ingredientes =  listar_ingredientes()
        if listado_ingredientes:
            for ingrediente in listado_ingredientes:
                tabla.add_row([ingrediente.id_ingrediente, ingrediente.nombre, ingrediente.unidad_medida])
                return tabla