from datetime import date
from datos.modelos.receta import Receta
from datos.modelos.usuario import usuario as Usuario


def listar_recetas():
    try:
        return list(
            Receta.select(Receta, Usuario)
            .join(Usuario)
            .order_by(Receta.id_receta)
        )
    except Exception as error:
        print(f"Error al listar recetas: {error}")
        return []


def obtener_receta_por_id(id_receta):
    try:
        return (
            Receta.select(Receta, Usuario)
            .join(Usuario)
            .where(Receta.id_receta == id_receta)
            .get()
        )
    except Receta.DoesNotExist:
        print(f"Receta con ID {id_receta} no encontrada.")
        return None
    except Exception as error:
        print(f"Error al obtener receta: {error}")
        return None


def agregar_receta(id_usuario, nombre, descripcion, tiempo_preparacion, dificultad, instrucciones):
    try:
        return Receta.create(
            usuario=id_usuario,
            nombre=nombre,
            descripcion=descripcion,
            tiempo_preparacion=tiempo_preparacion,
            dificultad=dificultad,
            instrucciones=instrucciones,
            fecha_publicacion=date.today(),
        )
    except Exception as error:
        print(f"Error al agregar receta: {error}")
        return None


def actualizar_receta(id_receta, nombre, descripcion, tiempo_preparacion, dificultad, instrucciones):
    try:
        receta = Receta.get_by_id(id_receta)
        receta.nombre = nombre
        receta.descripcion = descripcion
        receta.tiempo_preparacion = tiempo_preparacion
        receta.dificultad = dificultad
        receta.instrucciones = instrucciones
        receta.save()
        return receta
    except Receta.DoesNotExist:
        print(f"Receta con ID {id_receta} no encontrada.")
        return None
    except Exception as error:
        print(f"Error al actualizar receta: {error}")
        return None


def eliminar_receta(id_receta):
    try:
        receta = Receta.get_by_id(id_receta)
        receta.delete_instance()
        return True
    except Receta.DoesNotExist:
        print(f"Receta con ID {id_receta} no encontrada.")
        return False
    except Exception as error:
        print(f"Error al eliminar receta: {error}")
        return False
