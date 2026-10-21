import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from auxiliares.datos_app import nombre_app, version_app
from negocio.negocio_ingredientes import procesar_listado_ingredientes, procesar_nuevo_ingrediente, procesar_actualizacion_ingrediente, procesar_eliminacion_ingrediente

def mostrar_opciones():
    print(f"\n--- Menú Principal {nombre_app} v{version_app} ---")
    print("1. Leer/Listar registros")
    print("2. Crear nuevo registro")
    print("3. Actualizar registro")
    print("4. Eliminar registro")
    print("0. Salir")

def iniciar_menu():
    while True:
        mostrar_opciones()
        opcion = input("Seleccione una operación (1-5): ")

        match opcion:
            case '1':
                print("\n[Ejecutando: SELECT - Listando registros...]")
                procesar_listado_ingredientes()
            case '2':
                print("\n[Ejecutando: INSERT - Agregando nuevo registro...]")
                procesar_nuevo_ingrediente()
            case '3':
                print("\n[Ejecutando: UPDATE - Actualizando registro...]")
                id_ingrediente = input("Ingrese el ID del ingrediente: ")
                nombre = input("Ingrese el nuevo nombre: ")
                unidad_medida = input("Ingrese la nueva unidad de medida: ")
                procesar_actualizacion_ingrediente(id_ingrediente, nombre, unidad_medida)
            case '4':
                print("\n[Ejecutando: DELETE - Eliminando registro...]")
                id_ingrediente = input("Ingrese el ID del ingrediente: ")
                procesar_eliminacion_ingrediente(id_ingrediente)
            case '0':
                print("\nCerrando el sistema de la API...")
                break
            case _:
                print("\nOpción no válida. Por favor, seleccione un número del 0 al 4.")


                    
    