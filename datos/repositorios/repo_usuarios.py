from datetime import date
from datos.modelos.models import Usuario

def listar_usuarios():
    try:
        return list(Usuario.select().order_by(Usuario.id_usuario))
    except Exception as error:
        print(f"Error al listar usuarios: {error}")
        return []

def validar_email(email):
    try:
        return Usuario.select().where(Usuario.email == email).exists()
    except Exception as error:
        print(f"Error al validar email: {error}")
        return False

def agregar_usuario(nombre, email, contrasena, rut):
    if validar_email(email):
        print(f"El email {email} ya está en uso.")
        return None

    try:
        nuevo_usuario = Usuario.create(
            nombre=nombre,
            email=email,
            contrasena=contrasena,
            rut=rut,
            fecha_registro=date.today(),
            popularidad=0
        )
        return nuevo_usuario
    except Exception as error:
        print(f"Error al agregar usuario: {error}")
        return None

def actualizar_usuario(id_usuario, nombre, email, contrasena, rut):
    try:
        usuario_existente = Usuario.get_by_id(id_usuario)
        usuario_existente.nombre = nombre
        usuario_existente.email = email
        usuario_existente.contrasena = contrasena
        usuario_existente.rut = rut
        usuario_existente.save()
        return usuario_existente
    except Usuario.DoesNotExist:
        print(f"Usuario con ID {id_usuario} no encontrado.")
        return None
    except Exception as error:
        print(f"Error al actualizar usuario: {error}")
        return None

def eliminar_usuario(id_usuario):
    try:
        usuario_existente = Usuario.get_by_id(id_usuario)
        usuario_existente.delete_instance()
        return True
    except Usuario.DoesNotExist:
        print(f"Usuario con ID {id_usuario} no encontrado.")
        return False
    except Exception as error:
        print(f"Error al eliminar usuario: {error}")
        return False

def obtener_usuario_por_id(id_usuario):
    try:
        usuario_encontrado = Usuario.get_by_id(id_usuario)
        return {
            "id_usuario": usuario_encontrado.id_usuario,
            "nombre": usuario_encontrado.nombre,
            "email": usuario_encontrado.email,
            "contrasena": usuario_encontrado.contrasena,
            "rut": usuario_encontrado.rut,
            "fecha_registro": usuario_encontrado.fecha_registro.isoformat() if usuario_encontrado.fecha_registro else None,
            "popularidad": usuario_encontrado.popularidad,
        }
    except Usuario.DoesNotExist:
        print(f"Usuario con ID {id_usuario} no encontrado.")
        return None
    except Exception as error:
        print(f"Error al obtener usuario por ID: {error}")
        return None

def obtener_usuario_por_email(email):
    try:
        return Usuario.get(Usuario.email == email)
    except Usuario.DoesNotExist:
        print(f"Usuario con email {email} no encontrado.")
        return None
    except Exception as error:
        print(f"Error al obtener usuario por email: {error}")
        return None

def actualizar_popularidad_usuario(id_usuario, nueva_popularidad):
    try:
        usuario_existente = Usuario.get_by_id(id_usuario)
        usuario_existente.popularidad = nueva_popularidad
        usuario_existente.save()
        return usuario_existente
    except Usuario.DoesNotExist:
        print(f"Usuario con ID {id_usuario} no encontrado.")
        return None
    except Exception as error:
        print(f"Error al actualizar popularidad del usuario: {error}")
        return None

def buscar_usuario_por_email(email):
    """Igual que obtener_usuario_por_email pero sin imprimir si no existe (para el login)."""
    try:
        return Usuario.get_or_none(Usuario.email == email)
    except Exception as error:
        print(f"Error al buscar usuario por email: {error}")
        return None
