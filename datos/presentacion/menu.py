from prettytable import PrettyTable
from datos.auxiliares.datos_app import nombre_app, version_app
from datos.negocio.negocio_ingredientes import procesar_listado_ingredientes, procesar_nuevo_ingrediente, procesar_actualizacion_ingrediente, procesar_eliminacion_ingrediente
from datos.negocio.negocio_usuarios import procesar_listado_usuarios, crear_usuario, autenticar_usuario, actualizar_usuario_existente, eliminar_usuario_existente, obtener_usuario_por_id
from datos.negocio.negocio_recetas import procesar_listado_recetas, procesar_detalle_receta, procesar_nueva_receta, procesar_actualizacion_receta, procesar_eliminacion_receta
from datos.negocio.negocio_categorias import procesar_listado_categorias, procesar_nueva_categoria, procesar_actualizacion_categoria, procesar_eliminacion_categoria
from datos.negocio.negocio_comentarios import procesar_listado_comentarios, procesar_nuevo_comentario, procesar_actualizacion_comentario, procesar_eliminacion_comentario
from datos.negocio.negocio_valoraciones import procesar_listado_valoraciones, procesar_nueva_valoracion, procesar_actualizacion_valoracion, procesar_eliminacion_valoracion
from datos.negocio.negocio_guardados import procesar_listado_guardados, procesar_nuevo_guardado, procesar_actualizacion_guardado, procesar_eliminacion_guardado
from datos.negocio.negocio_receta_categorias import procesar_listado_receta_categorias, procesar_nueva_receta_categoria, procesar_actualizacion_receta_categoria, procesar_eliminacion_receta_categoria
from datos.negocio.negocio_receta_ingredientes import procesar_listado_receta_ingredientes, procesar_nuevo_receta_ingrediente, procesar_actualizacion_receta_ingrediente, procesar_eliminacion_receta_ingrediente
from getpass import getpass
from datos.auxiliares.sesion import iniciar_sesion, cerrar_sesion, obtener_usuario_actual
from datos.auxiliares.validaciones import validar_formato_contrasena, validar_rut

def pedir_contrasena(mensaje="Ingrese la contraseña del usuario", opcional=False):
    """Pide la contraseña (oculta), la valida y pide confirmación.
    Retorna la contraseña, o None si el usuario cancela (Enter vacío)."""
    while True:
        contrasena = getpass(f"{mensaje}{' (Enter para mantener la actual)' if opcional else ''}: ")
        if contrasena == "":
            if not opcional:
                print("Operación cancelada.")
            return "" if opcional else None
        if not validar_formato_contrasena(contrasena):
            continue
        if getpass("Confirme la contraseña: ") == contrasena:
            return contrasena
        print("Las contraseñas no coinciden. Intente nuevamente.")

def registrar_usuario():
    nombre = input("Ingrese el nombre del usuario: ")
    email = input("Ingrese el email del usuario: ")
    contrasena = pedir_contrasena()
    if contrasena is None:
        return None
    rut = validar_rut(None)
    return crear_usuario(nombre, email, contrasena, rut)

def pantalla_acceso():
    """Login / registro. Retorna True si se inició sesión, False si el usuario sale."""
    while True:
        print(f"\n--- Acceso {nombre_app} v{version_app} ---")
        print("1. Iniciar sesión")
        print("2. Registrarse")
        print("0. Salir")
        opcion = input("Seleccione una opción (0-2): ")

        match opcion:
            case '1':
                for intento in range(3):
                    email = input("Email: ")
                    contrasena = getpass("Contraseña: ")
                    usuario_autenticado = autenticar_usuario(email, contrasena)
                    if usuario_autenticado:
                        iniciar_sesion(usuario_autenticado)
                        print(f"\n¡Bienvenido/a, {usuario_autenticado.nombre}!")
                        return True
                    if intento < 2:
                        print(f"Intento {intento + 1} de 3.")
                print("Demasiados intentos fallidos.")
            case '2':
                print("\n[Registro de nuevo usuario]")
                registrar_usuario()
            case '0':
                return False
            case _:
                print("\nOpción no válida. Por favor, seleccione un número del 0 al 2.")

def mostrar_opciones():
    actual = obtener_usuario_actual()
    sesion = f" | Sesión: {actual.nombre}" if actual else ""
    print(f"\n--- Menú Principal {nombre_app} v{version_app}{sesion} ---")
    print("1. Gestionar ingredientes")
    print("2. Gestionar usuarios")
    print("3. Gestionar recetas")
    print("4. Gestionar categorías")
    print("5. Gestionar comentarios")
    print("6. Gestionar valoraciones")
    print("7. Gestionar recetas guardadas")
    print("8. Gestionar categorías de una receta")
    print("9. Gestionar ingredientes de una receta")
    print("10. Cerrar sesión")
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
                registrar_usuario()
            case '3':
                print("\n[Ejecutando: UPDATE - Actualizando usuario...]")
                print(procesar_listado_usuarios())
                id_usuario = input("Ingrese el ID del usuario que desea actualizar: ")
                nombre = input("Ingrese el nuevo nombre: ")
                email = input("Ingrese el nuevo email: ")
                contrasena = pedir_contrasena("Ingrese la nueva contraseña", opcional=True)
                rut = input("Ingrese el nuevo RUT: ")
                actualizar_usuario_existente(id_usuario, nombre, email, contrasena, rut)
            case '4':
                print("\n[Ejecutando: DELETE - Eliminando usuario...]")
                print(procesar_listado_usuarios())
                id_usuario = input("Ingrese el ID del usuario: ")
                actual = obtener_usuario_actual()
                if actual and str(actual.id_usuario) == id_usuario.strip():
                    print("No puede eliminar el usuario con la sesión activa.")
                    continue
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

def gestionar_recetas():
    while True:
        print("\n--- Gestión de recetas ---")
        print("1. Leer/Listar recetas")
        print("2. Crear nueva receta")
        print("3. Actualizar receta")
        print("4. Eliminar receta")
        print("5. Ver detalle de una receta")
        print("0. Volver al menú principal")
        opcion = input("Seleccione una operación (0-5): ")

        match opcion:
            case '1':
                print("\n[Ejecutando: SELECT - Listando recetas...]")
                print(procesar_listado_recetas())
            case '2':
                print("\n[Ejecutando: INSERT - Agregando nueva receta...]")
                print(procesar_listado_usuarios())
                id_usuario = input("Ingrese el ID del usuario autor: ")
                nombre = input("Ingrese el nombre de la receta: ")
                descripcion = input("Ingrese la descripción (opcional): ")
                tiempo = input("Ingrese el tiempo de preparación (minutos): ")
                dificultad = input("Ingrese la dificultad (facil/media/dificil): ")
                instrucciones = input("Ingrese las instrucciones: ")
                procesar_nueva_receta(id_usuario, nombre, descripcion, tiempo, dificultad, instrucciones)
            case '3':
                print("\n[Ejecutando: UPDATE - Actualizando receta...]")
                print(procesar_listado_recetas())
                id_receta = input("Ingrese el ID de la receta que desea actualizar: ")
                nombre = input("Ingrese el nuevo nombre: ")
                descripcion = input("Ingrese la nueva descripción (opcional): ")
                tiempo = input("Ingrese el nuevo tiempo de preparación (minutos): ")
                dificultad = input("Ingrese la nueva dificultad (facil/media/dificil): ")
                instrucciones = input("Ingrese las nuevas instrucciones: ")
                procesar_actualizacion_receta(id_receta, nombre, descripcion, tiempo, dificultad, instrucciones)
            case '4':
                print("\n[Ejecutando: DELETE - Eliminando receta...]")
                print(procesar_listado_recetas())
                id_receta = input("Ingrese el ID de la receta: ")
                confirmacion = input("¿Está seguro de que desea eliminar la receta? (s/n): ")
                if confirmacion.lower() == 's':
                    procesar_eliminacion_receta(id_receta)
                else:
                    print("Operación de eliminación cancelada.")
            case '5':
                print(procesar_listado_recetas())
                id_receta = input("Ingrese el ID de la receta: ")
                detalle = procesar_detalle_receta(id_receta)
                if detalle:
                    print(detalle)
            case '0':
                break
            case _:
                print("\nOpción no válida. Por favor, seleccione un número del 0 al 5.")

def gestionar_categorias():
    while True:
        print("\n--- Gestión de categorías ---")
        print("1. Leer/Listar categorías")
        print("2. Crear nueva categoría")
        print("3. Actualizar categoría")
        print("4. Eliminar categoría")
        print("0. Volver al menú principal")
        opcion = input("Seleccione una operación (0-4): ")

        match opcion:
            case '1':
                print("\n[Ejecutando: SELECT - Listando categorías...]")
                print(procesar_listado_categorias())
            case '2':
                print("\n[Ejecutando: INSERT - Agregando nueva categoría...]")
                nombre = input("Ingrese el nombre de la categoría: ")
                tipo_comida = input("Ingrese el tipo de comida: ")
                procesar_nueva_categoria(nombre, tipo_comida)
            case '3':
                print("\n[Ejecutando: UPDATE - Actualizando categoría...]")
                print(procesar_listado_categorias())
                id_categoria = input("Ingrese el ID de la categoría: ")
                nombre = input("Ingrese el nuevo nombre: ")
                tipo_comida = input("Ingrese el nuevo tipo de comida: ")
                procesar_actualizacion_categoria(id_categoria, nombre, tipo_comida)
            case '4':
                print("\n[Ejecutando: DELETE - Eliminando categoría...]")
                print(procesar_listado_categorias())
                id_categoria = input("Ingrese el ID de la categoría: ")
                confirmacion = input("¿Está seguro de que desea eliminar la categoría? (s/n): ")
                if confirmacion.lower() == 's':
                    procesar_eliminacion_categoria(id_categoria)
                else:
                    print("Operación de eliminación cancelada.")
            case '0':
                break
            case _:
                print("\nOpción no válida. Por favor, seleccione un número del 0 al 4.")

def gestionar_comentarios():
    while True:
        print("\n--- Gestión de comentarios ---")
        print("1. Leer/Listar comentarios")
        print("2. Crear nuevo comentario")
        print("3. Actualizar comentario")
        print("4. Eliminar comentario")
        print("0. Volver al menú principal")
        opcion = input("Seleccione una operación (0-4): ")

        match opcion:
            case '1':
                print("\n[Ejecutando: SELECT - Listando comentarios...]")
                print(procesar_listado_comentarios())
            case '2':
                print("\n[Ejecutando: INSERT - Agregando nuevo comentario...]")
                print(procesar_listado_usuarios())
                id_usuario = input("Ingrese el ID del usuario: ")
                print(procesar_listado_recetas())
                id_receta = input("Ingrese el ID de la receta: ")
                texto = input("Ingrese el comentario: ")
                procesar_nuevo_comentario(id_usuario, id_receta, texto)
            case '3':
                print("\n[Ejecutando: UPDATE - Actualizando comentario...]")
                print(procesar_listado_comentarios())
                id_comentario = input("Ingrese el ID del comentario: ")
                texto = input("Ingrese el nuevo texto: ")
                procesar_actualizacion_comentario(id_comentario, texto)
            case '4':
                print("\n[Ejecutando: DELETE - Eliminando comentario...]")
                print(procesar_listado_comentarios())
                id_comentario = input("Ingrese el ID del comentario: ")
                confirmacion = input("¿Está seguro de que desea eliminar el comentario? (s/n): ")
                if confirmacion.lower() == 's':
                    procesar_eliminacion_comentario(id_comentario)
                else:
                    print("Operación de eliminación cancelada.")
            case '0':
                break
            case _:
                print("\nOpción no válida. Por favor, seleccione un número del 0 al 4.")

def gestionar_valoraciones():
    while True:
        print("\n--- Gestión de valoraciones ---")
        print("1. Leer/Listar valoraciones")
        print("2. Crear nueva valoración")
        print("3. Actualizar valoración")
        print("4. Eliminar valoración")
        print("0. Volver al menú principal")
        opcion = input("Seleccione una operación (0-4): ")

        match opcion:
            case '1':
                print("\n[Ejecutando: SELECT - Listando valoraciones...]")
                print(procesar_listado_valoraciones())
            case '2':
                print("\n[Ejecutando: INSERT - Agregando nueva valoración...]")
                print(procesar_listado_usuarios())
                id_usuario = input("Ingrese el ID del usuario: ")
                print(procesar_listado_recetas())
                id_receta = input("Ingrese el ID de la receta: ")
                puntuacion = input("Ingrese la puntuación (1-5): ")
                procesar_nueva_valoracion(id_usuario, id_receta, puntuacion)
            case '3':
                print("\n[Ejecutando: UPDATE - Actualizando valoración...]")
                print(procesar_listado_valoraciones())
                id_valoracion = input("Ingrese el ID de la valoración: ")
                puntuacion = input("Ingrese la nueva puntuación (1-5): ")
                procesar_actualizacion_valoracion(id_valoracion, puntuacion)
            case '4':
                print("\n[Ejecutando: DELETE - Eliminando valoración...]")
                print(procesar_listado_valoraciones())
                id_valoracion = input("Ingrese el ID de la valoración: ")
                confirmacion = input("¿Está seguro de que desea eliminar la valoración? (s/n): ")
                if confirmacion.lower() == 's':
                    procesar_eliminacion_valoracion(id_valoracion)
                else:
                    print("Operación de eliminación cancelada.")
            case '0':
                break
            case _:
                print("\nOpción no válida. Por favor, seleccione un número del 0 al 4.")

def gestionar_guardados():
    while True:
        print("\n--- Gestión de recetas guardadas ---")
        print("1. Leer/Listar guardados")
        print("2. Guardar una receta")
        print("3. Actualizar guardado")
        print("4. Eliminar guardado")
        print("0. Volver al menú principal")
        opcion = input("Seleccione una operación (0-4): ")

        match opcion:
            case '1':
                print("\n[Ejecutando: SELECT - Listando guardados...]")
                print(procesar_listado_guardados())
            case '2':
                print("\n[Ejecutando: INSERT - Guardando receta...]")
                print(procesar_listado_usuarios())
                id_usuario = input("Ingrese el ID del usuario: ")
                print(procesar_listado_recetas())
                id_receta = input("Ingrese el ID de la receta: ")
                procesar_nuevo_guardado(id_usuario, id_receta)
            case '3':
                print("\n[Ejecutando: UPDATE - Actualizando guardado...]")
                print(procesar_listado_guardados())
                id_guardado = input("Ingrese el ID del guardado: ")
                print(procesar_listado_usuarios())
                id_usuario = input("Ingrese el nuevo ID de usuario: ")
                print(procesar_listado_recetas())
                id_receta = input("Ingrese el nuevo ID de receta: ")
                procesar_actualizacion_guardado(id_guardado, id_usuario, id_receta)
            case '4':
                print("\n[Ejecutando: DELETE - Eliminando guardado...]")
                print(procesar_listado_guardados())
                id_guardado = input("Ingrese el ID del guardado: ")
                confirmacion = input("¿Está seguro de que desea eliminar el guardado? (s/n): ")
                if confirmacion.lower() == 's':
                    procesar_eliminacion_guardado(id_guardado)
                else:
                    print("Operación de eliminación cancelada.")
            case '0':
                break
            case _:
                print("\nOpción no válida. Por favor, seleccione un número del 0 al 4.")

def gestionar_receta_categorias():
    while True:
        print("\n--- Gestión de categorías de una receta ---")
        print("1. Leer/Listar categorías por receta")
        print("2. Asignar categoría a una receta")
        print("3. Cambiar categoría de una receta")
        print("4. Quitar categoría de una receta")
        print("0. Volver al menú principal")
        opcion = input("Seleccione una operación (0-4): ")

        match opcion:
            case '1':
                print("\n[Ejecutando: SELECT - Listando categorías por receta...]")
                print(procesar_listado_receta_categorias())
            case '2':
                print("\n[Ejecutando: INSERT - Asignando categoría...]")
                print(procesar_listado_recetas())
                id_receta = input("Ingrese el ID de la receta: ")
                print(procesar_listado_categorias())
                id_categoria = input("Ingrese el ID de la categoría: ")
                procesar_nueva_receta_categoria(id_receta, id_categoria)
            case '3':
                print("\n[Ejecutando: UPDATE - Cambiando categoría...]")
                print(procesar_listado_receta_categorias())
                id_receta = input("Ingrese el ID de la receta: ")
                id_categoria_actual = input("Ingrese el ID de la categoría actual: ")
                print(procesar_listado_categorias())
                id_categoria_nueva = input("Ingrese el ID de la nueva categoría: ")
                procesar_actualizacion_receta_categoria(id_receta, id_categoria_actual, id_categoria_nueva)
            case '4':
                print("\n[Ejecutando: DELETE - Quitando categoría...]")
                print(procesar_listado_receta_categorias())
                id_receta = input("Ingrese el ID de la receta: ")
                id_categoria = input("Ingrese el ID de la categoría: ")
                confirmacion = input("¿Está seguro de que desea quitar la categoría de la receta? (s/n): ")
                if confirmacion.lower() == 's':
                    procesar_eliminacion_receta_categoria(id_receta, id_categoria)
                else:
                    print("Operación de eliminación cancelada.")
            case '0':
                break
            case _:
                print("\nOpción no válida. Por favor, seleccione un número del 0 al 4.")

def gestionar_receta_ingredientes():
    while True:
        print("\n--- Gestión de ingredientes de una receta ---")
        print("1. Leer/Listar ingredientes por receta")
        print("2. Asignar ingrediente a una receta")
        print("3. Actualizar cantidad de un ingrediente")
        print("4. Quitar ingrediente de una receta")
        print("0. Volver al menú principal")
        opcion = input("Seleccione una operación (0-4): ")

        match opcion:
            case '1':
                print("\n[Ejecutando: SELECT - Listando ingredientes por receta...]")
                print(procesar_listado_receta_ingredientes())
            case '2':
                print("\n[Ejecutando: INSERT - Asignando ingrediente...]")
                print(procesar_listado_recetas())
                id_receta = input("Ingrese el ID de la receta: ")
                print(procesar_listado_ingredientes(PrettyTable()))
                id_ingrediente = input("Ingrese el ID del ingrediente: ")
                cantidad = input("Ingrese la cantidad: ")
                procesar_nuevo_receta_ingrediente(id_receta, id_ingrediente, cantidad)
            case '3':
                print("\n[Ejecutando: UPDATE - Actualizando cantidad...]")
                print(procesar_listado_receta_ingredientes())
                id_receta = input("Ingrese el ID de la receta: ")
                id_ingrediente = input("Ingrese el ID del ingrediente: ")
                cantidad = input("Ingrese la nueva cantidad: ")
                procesar_actualizacion_receta_ingrediente(id_receta, id_ingrediente, cantidad)
            case '4':
                print("\n[Ejecutando: DELETE - Quitando ingrediente...]")
                print(procesar_listado_receta_ingredientes())
                id_receta = input("Ingrese el ID de la receta: ")
                id_ingrediente = input("Ingrese el ID del ingrediente: ")
                confirmacion = input("¿Está seguro de que desea quitar el ingrediente de la receta? (s/n): ")
                if confirmacion.lower() == 's':
                    procesar_eliminacion_receta_ingrediente(id_receta, id_ingrediente)
                else:
                    print("Operación de eliminación cancelada.")
            case '0':
                break
            case _:
                print("\nOpción no válida. Por favor, seleccione un número del 0 al 4.")

def iniciar_menu():
    if not pantalla_acceso():
        print("\nCerrando el sistema de la API...")
        return
    while True:
        mostrar_opciones()
        opcion = input("Seleccione una operación (0-10): ")

        match opcion:
            case '1':
                gestionar_ingredientes()
            case '2':
                gestionar_usuarios()
            case '3':
                gestionar_recetas()
            case '4':
                gestionar_categorias()
            case '5':
                gestionar_comentarios()
            case '6':
                gestionar_valoraciones()
            case '7':
                gestionar_guardados()
            case '8':
                gestionar_receta_categorias()
            case '9':
                gestionar_receta_ingredientes()
            case '10':
                cerrar_sesion()
                print("\nSesión cerrada.")
                if not pantalla_acceso():
                    print("\nCerrando el sistema de la API...")
                    break
            case '0':
                print("\nCerrando el sistema de la API...")
                break
            case _:
                print("\nOpción no válida. Por favor, seleccione un número del 0 al 10.")


                    
    