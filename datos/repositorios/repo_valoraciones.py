from datetime import date
from datos.modelos.valoracion import Valoracion
from datos.modelos.receta import Receta
from datos.modelos.usuario import usuario as Usuario


def listar_valoraciones():
    try:
        return list(
            Valoracion.select(Valoracion, Usuario, Receta)
            .join(Usuario)
            .switch(Valoracion)
            .join(Receta)
            .order_by(Valoracion.id_valoracion)
        )
    except Exception as error:
        print(f"Error al listar valoraciones: {error}")
        return []


def validar_valoracion(id_usuario, id_receta):
    try:
        return Valoracion.select().where(
            (Valoracion.usuario == id_usuario) & (Valoracion.receta == id_receta)
        ).exists()
    except Exception as error:
        print(f"Error al validar valoración: {error}")
        return False


def agregar_valoracion(id_usuario, id_receta, puntuacion):
    if validar_valoracion(id_usuario, id_receta):
        print("Este usuario ya valoró esta receta.")
        return None
    try:
        return Valoracion.create(
            usuario=id_usuario,
            receta=id_receta,
            puntuacion=puntuacion,
            fecha=date.today(),
        )
    except Exception as error:
        print(f"Error al agregar valoración: {error}")
        return None


def actualizar_valoracion(id_valoracion, puntuacion):
    try:
        valoracion = Valoracion.get_by_id(id_valoracion)
        valoracion.puntuacion = puntuacion
        valoracion.save()
        return valoracion
    except Valoracion.DoesNotExist:
        print(f"Valoración con ID {id_valoracion} no encontrada.")
        return None
    except Exception as error:
        print(f"Error al actualizar valoración: {error}")
        return None


def eliminar_valoracion(id_valoracion):
    try:
        valoracion = Valoracion.get_by_id(id_valoracion)
        valoracion.delete_instance()
        return True
    except Valoracion.DoesNotExist:
        print(f"Valoración con ID {id_valoracion} no encontrada.")
        return False
    except Exception as error:
        print(f"Error al eliminar valoración: {error}")
        return False
