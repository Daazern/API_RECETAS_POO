from prettytable import PrettyTable
from datos.auxiliares.datos_app import nombre_app, version_app
from datos.negocio.negocio_ingredientes import procesar_listado_ingredientes, procesar_nuevo_ingrediente, procesar_actualizacion_ingrediente, procesar_eliminacion_ingrediente
from datos.negocio.negocio_usuarios import procesar_listado_usuarios, crear_usuario, actualizar_usuario_existente, eliminar_usuario_existente, obtener_usuario_por_id
import bcrypt

def mostrar_opciones():
    print(f"\n--- Menú Principal {nombre_app} v{version_app} ---")
    print("1. Gestionar ingredientes")
    print("2. Gestionar usuarios")
    print("0. Salir")

def gestionar_ingredientes():
    while True:
        print("\n--- Gestión de ingredientes ---")
        print("1. Leer/Listar ingredientes")
        print("2. Crear nuevo ingrediente")
        print("3. Actualizar ingrediente")
        print("4. Eliminar ingrediente")
        print("0. Volver al menú principal")
        opcion = input("Seleccione una operación (0-4): ")

        match opcion:
            case '1':
                print("\n[Ejecutando: SELECT - Listando registros...]")
                print(procesar_listado_ingredientes(PrettyTable()))
            case '2':
                print("\n[Ejecutando: INSERT - Agregando nuevo registro...]")
                nombre = input("Ingrese el nombre del ingrediente: ")
                unidad_medida = input("Ingrese la unidad de medida: ")
                procesar_nuevo_ingrediente(nombre, unidad_medida)
            case '3':
                print("\n[Ejecutando: UPDATE - Actualizando registro...]")
                print(procesar_listado_ingredientes(PrettyTable()))
                id_ingrediente = input("Ingrese el ID del ingrediente: ")
                nombre = input("Ingrese el nuevo nombre: ")
                unidad_medida = input("Ingrese la nueva unidad de medida: ")
                procesar_actualizacion_ingrediente(id_ingrediente, nombre, unidad_medida)
            case '4':
                print("\n[Ejecutando: DELETE - Eliminando registro...]")
                print(procesar_listado_ingredientes(PrettyTable()))
                id_ingrediente = input("Ingrese el ID del ingrediente: ")
                confirmacion = input("¿Está seguro de que desea eliminar el ingrediente? (s/n): ")
                if confirmacion.lower() == 's':
                    procesar_eliminacion_ingrediente(id_ingrediente)
                else:
                    print("Operación de eliminación cancelada.")
            case '0':
                break
            case _:
                print("\nOpción no válida. Por favor, seleccione un número del 0 al 4.")

def gestionar_usuarios():
    while True:
        print("\n--- Gestión de usuarios ---")
        print("1. Leer/Listar usuarios")
        print("2. Crear nuevo usuario")
        print("3. Actualizar usuario")
        print("4. Eliminar usuario")
        print("0. Volver al menú principal")
        opcion = input("Seleccione una operación (0-4): ")

        match opcion:
            case '1':
                print("\n[Ejecutando: SELECT - Listando usuarios...]")
                print(procesar_listado_usuarios())
            case '2':
                print("\n[Ejecutando: INSERT - Agregando nuevo usuario...]")
                nombre = input("Ingrese el nombre del usuario: ")
                email = input("Ingrese el email del usuario: ")
                contrasena = input("Ingrese la contraseña del usuario: ")
                contrasena = bcrypt.hashpw(contrasena.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
                print("Por favor, confirme la contraseña del usuario.")
                while contrasena != validar_contrasena or contrasena == "":
                        validar_contrasena = input("Confirme la contraseña del usuario: ")
                        
                        break
                rut = input("Ingrese el RUT del usuario: ")
                crear_usuario(nombre, email, contrasena, rut)
            case '3':
                print("\n[Ejecutando: UPDATE - Actualizando usuario...]")
                print(procesar_listado_usuarios())
                id_usuario = input("Ingrese el ID del usuario que desea actualizar: ")
                nombre = input("Ingrese el nuevo nombre: ")
                email = input("Ingrese el nuevo email: ")
                contrasena = input("Ingrese la nueva contraseña: ")
                contrasena = bcrypt.hashpw(contrasena.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
                rut = input("Ingrese el nuevo RUT: ")
                actualizar_usuario_existente(id_usuario, nombre, email, contrasena, rut)
            case '4':
                print("\n[Ejecutando: DELETE - Eliminando usuario...]")
                print(procesar_listado_usuarios())
                id_usuario = input("Ingrese el ID del usuario: ")
                objeto_usuario = obtener_usuario_por_id(id_usuario)
                nombre_usuario = objeto_usuario.get("nombre", "desconocido") if objeto_usuario else "desconocido"
                rut_usuario = objeto_usuario.get("rut", "sin RUT") if objeto_usuario else "sin RUT"
                email_usuario = objeto_usuario.get("email", "sin correo") if objeto_usuario else "sin correo"
                confirmacion = input("¿Está seguro de que desea eliminar al usuario {} (RUT: {}, correo: {})? (s/n): ".format(nombre_usuario, rut_usuario, email_usuario))
                if confirmacion.lower() == 's':
                    eliminar_usuario_existente(id_usuario)
                else:
                    print("Operación de eliminación cancelada.")
            case '0':
                break
            case _:
                print("\nOpción no válida. Por favor, seleccione un número del 0 al 4.")

def iniciar_menu():
    while True:
        mostrar_opciones()
        opcion = input("Seleccione una operación (0-1): ")

        match opcion:
            case '1':
                gestionar_ingredientes()
            case '2':
                gestionar_usuarios()
            case '0':
                print("\nCerrando el sistema de la API...")
                break
            case _:
                print("\nOpción no válida. Por favor, seleccione un número del 0 al 2.")


                    
    