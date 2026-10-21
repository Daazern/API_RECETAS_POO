from auxiliares.datos_app import nombre_app, version_app

def mostrar_opciones():
    print("\n--- Menú Principal API Recetas ---")
    print("1. Leer/Listar registros")
    print("2. Crear nuevo registro")
    print("3. Actualizar registro")
    print("4. Eliminar registro")
    print("5. Salir")

def iniciar_menu():
    while True:
        mostrar_opciones()
        opcion = input("Seleccione una operación (1-5): ")

        match opcion:
            case '1':
                print("\n[Ejecutando: SELECT - Listando registros...]")
                # Ejemplo: repo_ingredientes.obtener_todos()
            case '2':
                print("\n[Ejecutando: INSERT - Agregando nuevo registro...]")
                # Ejemplo: repo_ingredientes.crear(nuevo_ingrediente)
            case '3':
                print("\n[Ejecutando: UPDATE - Actualizando registro...]")
                # Ejemplo: repo_ingredientes.actualizar(id, datos)
            case '4':
                print("\n[Ejecutando: DELETE - Eliminando registro...]")
                # Ejemplo: repo_ingredientes.eliminar(id)
            case '5':
                print("\nCerrando el sistema de la API...")
                break
            case _:
                print("\nOpción no válida. Por favor, seleccione un número del 1 al 5.")
    