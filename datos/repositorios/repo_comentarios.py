from datetime import date
from datos.modelos.comentario import Comentario
from datos.modelos.receta import Receta
from datos.modelos.usuario import usuario as Usuario


def listar_comentarios():
    try:
        return list(
            Comentario.select(Comentario, Usuario, Receta)
            .join(Usuario)
            .switch(Comentario)
            .join(Receta)
            .order_by(Comentario.id_comentario)
        )
    except Exception as error:
        print(f"Error al listar comentarios: {error}")
        return []


def agregar_comentario(id_usuario, id_receta, texto):
    try:
        return Comentario.create(
            usuario=id_usuario,
            receta=id_receta,
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
