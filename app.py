import prettytable

from datos.negocio.negocio_ingredientes import procesar_listado_ingredientes

from datos.presentacion.menu import cargar_menu

tabla_ingredientes = prettytable.PrettyTable()
cargar_menu()
tabla_ingredientes = procesar_listado_ingredientes(tabla_ingredientes)

tabla_ingredientes = prettytable.PrettyTable()
ingredientes = procesar_listado_ingredientes(tabla_ingredientes)
for ingrediente in ingredientes:
    print(ingrediente.id_ingrediente, ingrediente.nombre, ingrediente.unidad_medida)

nuevo_ingrediente = procesar_listado_ingredientes()
nuevo_ingrediente.nombre = "Tomate"
nuevo_ingrediente.unidad_medida = "Unidad"
nuevo_ingrediente.save()   

ingredientes = procesar_listado_ingredientes(tabla_ingredientes)
for ingrediente in ingredientes:
    print(ingrediente.id_ingrediente, ingrediente.nombre, ingrediente.unidad_medida)