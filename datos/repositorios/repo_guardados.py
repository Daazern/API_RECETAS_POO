from datetime import date
from datos.modelos.guardado import Guardado
from datos.modelos.receta import Receta
from datos.modelos.usuario import usuario as Usuario


def listar_guardados():
    try:
        return list(
            Guardado.select(Guardado, Usuario, Receta)
            .join(Usuario)
            .switch(Guardado)
            .join(Receta)
            .order_by(Guardado.id_guardado)
        )
    except Exception as error:
        print(f"Error al listar guardados: {error}")
        return []


def validar_guardado(id_usuario, id_receta):
    try:
        return Guardado.select().where(
            (Guardado.usuario == id_usuario) & (Guardado.receta == id_receta)
        ).exists()
    except Exception as error:
        print(f"Error al validar guardado: {error}")
        return False


def agregar_guardado(id_usuario, id_receta):
    if validar_guardado(id_usuario, id_receta):
        print("Este usuario ya guardó esta receta.")
        return None
    try:
        return Guardado.create(
            usuario=id_usuario,
            receta=id_receta,
            fecha_guardado=date.today(),
        )
    except Exception as error:
        print(f"Error al agregar guardado: {error}")
        return None


def actualizar_guardado(id_guardado, id_usuario, id_receta):
    try:
        guardado = Guardado.get_by_id(id_guardado)
        existe_otro = Guardado.select().where(
            (Guardado.usuario == id_usuario)
            & (Guardado.receta == id_receta)
            & (Guardado.id_guardado != id_guardado)
        ).exists()
        if existe_otro:
            print("Este usuario ya guardó esa receta.")
            return None
        guardado.usuario = id_usuario
        guardado.receta = id_receta
        guardado.save()
        return guardado
    except Guardado.DoesNotExist:
        print(f"Guardado con ID {id_guardado} no encontrado.")
        return None
    except Exception as error:
        print(f"Error al actualizar guardado: {error}")
        return None


def eliminar_guardado(id_guardado):
    try:
        guardado = Guardado.get_by_id(id_guardado)
        guardado.delete_instance()
        return True
    except Guardado.DoesNotExist:
        print(f"Guardado con ID {id_guardado} no encontrado.")
        return False
    except Exception as error:
        print(f"Error al eliminar guardado: {error}")
        return False
