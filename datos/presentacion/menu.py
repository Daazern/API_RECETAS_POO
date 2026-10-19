from auxiliares.datos_app import nombre_app, version_app

def cargar_menu():
    menu = {
        'nombre_app': nombre_app,
        'version_app': version_app,
        'opciones': [
            {'opcion': 1, 'descripcion': 'Listar recetas'},
            {'opcion': 2, 'descripcion': 'Listar ingredientes'},
            {'opcion': 3, 'descripcion': 'Buscar receta por nombre'},
            {'opcion': 4, 'descripcion': 'Buscar receta por categoría'},
            {'opcion': 5, 'descripcion': 'Agregar nueva receta'},
            {'opcion': 6, 'descripcion': 'Actualizar receta existente'},
            {'opcion': 7, 'descripcion': 'Eliminar receta'},
            {'opcion': 8, 'descripcion': 'Salir'}
        ]
    }

    print("=" * 40)
    print(f"{menu['nombre_app']} - v{menu['version_app']}")
    print("=" * 40)

    for item in menu['opciones']:
        print(f"{item['opcion']}. {item['descripcion']}")

    print("=" * 40)