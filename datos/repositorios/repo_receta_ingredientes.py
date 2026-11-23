from datos.modelos.receta_ingrediente import RecetaIngrediente
from datos.modelos.receta import Receta
from datos.modelos.ingredientes import Ingrediente


def listar_receta_ingredientes():
    try:
        return list(
            RecetaIngrediente.select(RecetaIngrediente, Receta, Ingrediente)
            .join(Receta)
            .switch(RecetaIngrediente)
            .join(Ingrediente)
            .order_by(RecetaIngrediente.receta, RecetaIngrediente.ingrediente)
        )
    except Exception as error:
        print(f"Error al listar ingredientes de recetas: {error}")
        return []


def validar_receta_ingrediente(id_receta, id_ingrediente):
    try:
        return RecetaIngrediente.select().where(
            (RecetaIngrediente.receta == id_receta) & (RecetaIngrediente.ingrediente == id_ingrediente)
        ).exists()
    except Exception as error:
        print(f"Error al validar ingrediente de receta: {error}")
        return False


def agregar_receta_ingrediente(id_receta, id_ingrediente, cantidad):
    if validar_receta_ingrediente(id_receta, id_ingrediente):
        print("Esa receta ya tiene asignado ese ingrediente.")
        return None
    try:
        return RecetaIngrediente.create(receta=id_receta, ingrediente=id_ingrediente, cantidad=cantidad)
    except Exception as error:
        print(f"Error al asignar ingrediente a la receta: {error}")
        return None


def actualizar_receta_ingrediente(id_receta, id_ingrediente, cantidad):
    try:
        filas = (RecetaIngrediente
            .update(cantidad=cantidad)
            .where((RecetaIngrediente.receta == id_receta) & (RecetaIngrediente.ingrediente == id_ingrediente))
            .execute())
        if filas == 0 and not validar_receta_ingrediente(id_receta, id_ingrediente):
            print("Esa receta no tiene asignado el ingrediente indicado.")
            return False
        return True
    except Exception as error:
        print(f"Error al actualizar ingrediente de la receta: {error}")
        return False


def eliminar_receta_ingrediente(id_receta, id_ingrediente):
    try:
        filas = (RecetaIngrediente
            .delete()
            .where((RecetaIngrediente.receta == id_receta) & (RecetaIngrediente.ingrediente == id_ingrediente))
            .execute())
        if filas == 0:
            print("Esa receta no tiene asignado el ingrediente indicado.")
            return False
        return True
    except Exception as error:
        print(f"Error al eliminar ingrediente de la receta: {error}")
        return False
