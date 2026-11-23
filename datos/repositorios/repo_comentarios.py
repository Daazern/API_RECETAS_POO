from datetime import date
from datos.modelos.models import Comentario, Receta, Usuario


def listar_comentarios():
    try:
        return list(
            Comentario.select(Comentario, Usuario, Receta)
            .join(Usuario, on=(Comentario.id_usuario == Usuario.id_usuario), attr='usuario')
            .switch(Comentario)
            .join(Receta, on=(Comentario.id_receta == Receta.id_receta), attr='receta')
            .order_by(Comentario.id_comentario)
        )
    except Exception as error:
        print(f"Error al listar comentarios: {error}")
        return []


def agregar_comentario(id_usuario, id_receta, texto):
    try:
        return Comentario.create(
            id_usuario=id_usuario,
            id_receta=id_receta,
            texto=texto,
            fecha=date.today(),
        )
    except Exception as error:
        print(f"Error al agregar comentario: {error}")
        return None


def actualizar_comentario(id_comentario, texto):
    try:
        comentario = Comentario.get_by_id(id_comentario)
        comentario.texto = texto
        comentario.save()
        return comentario
    except Comentario.DoesNotExist:
        print(f"Comentario con ID {id_comentario} no encontrado.")
        return None
    except Exception as error:
        print(f"Error al actualizar comentario: {error}")
        return None


def eliminar_comentario(id_comentario):
    try:
        comentario = Comentario.get_by_id(id_comentario)
        comentario.delete_instance()
        return True
    except Comentario.DoesNotExist:
        print(f"Comentario con ID {id_comentario} no encontrado.")
        return False
    except Exception as error:
        print(f"Error al eliminar comentario: {error}")
        return False
