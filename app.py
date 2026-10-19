import prettytable

from datos.presentacion.menu import cargar_menu

tabla_ingredientes = prettytable.PrettyTable()
cargar_menu()

tabla_ingredientes = prettytable.PrettyTable()
ingredientes = listado_ingredientes()
for ingrediente in ingredientes:
    print(ingrediente.id_ingrediente, ingrediente.nombre, ingrediente.unidad_medida)

nuevo_ingrediente = Ingrediente()
nuevo_ingrediente.nombre = "Tomate"
nuevo_ingrediente.unidad_medida = "Unidad"
nuevo_ingrediente.save()   