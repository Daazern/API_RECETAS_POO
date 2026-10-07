from auxiliares.datos_app import nombre_app, version_app

def cargar_menu():
    menu = {
        'nombre_app': nombre_app,
        'version_app': version_app,
        'opciones': [
            {'opcion': 1, 'descripcion': 'Listar recetas'},
            {'opcion': 2, 'descripcion': 'Buscar receta por nombre'},
            {'opcion': 3, 'descripcion': 'Buscar receta por categoría'},
            {'opcion': 4, 'descripcion': 'Agregar nueva receta'},
            {'opcion': 5, 'descripcion': 'Actualizar receta existente'},
            {'opcion': 6, 'descripcion': 'Eliminar receta'},
            {'opcion': 7, 'descripcion': 'Salir'}
        ]
    }
    print(menu)