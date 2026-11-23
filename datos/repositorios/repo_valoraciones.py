from datetime import date
from datos.modelos.models import Valoracion, Receta, Usuario


def listar_valoraciones():
    try:
        return list(
            Valoracion.select(Valoracion, Usuario, Receta)
            .join(Usuario, on=(Valoracion.id_usuario == Usuario.id_usuario), attr='usuario')
            .switch(Valoracion)
            .join(Receta, on=(Valoracion.id_receta == Receta.id_receta), attr='receta')
            .order_by(Valoracion.id_valoracion)
        )
    except Exception as error:
        print(f"Error al listar valoraciones: {error}")
        return []


def validar_valoracion(id_usuario, id_receta):
    try:
        return Valoracion.select().where(
            (Valoracion.id_usuario == id_usuario) & (Valoracion.id_receta == id_receta)
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
            id_usuario=id_usuario,
            id_receta=id_receta,
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
