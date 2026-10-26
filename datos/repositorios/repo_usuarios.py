from datetime import date
from datos.modelos.usuario import usuario

def listar_usuarios():
    try:
        return list(usuario.select().order_by(usuario.id_usuario))
    except Exception as error:
        print(f"Error al listar usuarios: {error}")
        return []

def agregar_usuario(nombre, email, contrasena):
    try:
        nuevo_usuario = usuario.create(
            nombre=nombre,
            email=email,
            contrasena=contrasena,
            fecha_registro=date.today(),
            popularidad=0
        )
        return nuevo_usuario
    except Exception as error:
        print(f"Error al agregar usuario: {error}")
        return None

def actualizar_usuario(id_usuario, nombre, email, contrasena):
    try:
        usuario_existente = usuario.get_by_id(id_usuario)
        usuario_existente.nombre = nombre
        usuario_existente.email = email
        usuario_existente.contrasena = contrasena
        usuario_existente.save()
        return usuario_existente
    except usuario.DoesNotExist:
        print(f"Usuario con ID {id_usuario} no encontrado.")
        return None
    except Exception as error:
        print(f"Error al actualizar usuario: {error}")
        return None

def eliminar_usuario(id_usuario):
    try:
        usuario_existente = usuario.get_by_id(id_usuario)
        usuario_existente.delete_instance()
        return True
    except usuario.DoesNotExist:
        print(f"Usuario con ID {id_usuario} no encontrado.")
        return False
    except Exception as error:
        print(f"Error al eliminar usuario: {error}")
        return False

def obtener_usuario_por_id(id_usuario):
    try:
        return usuario.get_by_id(id_usuario)
    except usuario.DoesNotExist:
        print(f"Usuario con ID {id_usuario} no encontrado.")
        return None
    except Exception as error:
        print(f"Error al obtener usuario por ID: {error}")
        return None

def obtener_usuario_por_email(email):
    try:
        return usuario.get(usuario.email == email)
    except usuario.DoesNotExist:
        print(f"Usuario con email {email} no encontrado.")
        return None
    except Exception as error:
        print(f"Error al obtener usuario por email: {error}")
        return None

def actualizar_popularidad_usuario(id_usuario, nueva_popularidad):
    try:
        usuario_existente = usuario.get_by_id(id_usuario)
        usuario_existente.popularidad = nueva_popularidad
        usuario_existente.save()
        return usuario_existente
    except usuario.DoesNotExist:
        print(f"Usuario con ID {id_usuario} no encontrado.")
        return None
    except Exception as error:
        print(f"Error al actualizar popularidad del usuario: {error}")
        return None