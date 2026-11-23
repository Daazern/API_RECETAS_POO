from datos.modelos.models import RecetaIngrediente, Receta, Ingrediente


def listar_receta_ingredientes():
    try:
        return list(
            RecetaIngrediente.select(RecetaIngrediente, Receta, Ingrediente)
            .join(Receta, on=(RecetaIngrediente.id_receta == Receta.id_receta), attr='receta')
            .switch(RecetaIngrediente)
            .join(Ingrediente, on=(RecetaIngrediente.id_ingrediente == Ingrediente.id_ingrediente), attr='ingrediente')
            .order_by(RecetaIngrediente.id_receta, RecetaIngrediente.id_ingrediente)
        )
    except Exception as error:
        print(f"Error al listar ingredientes de recetas: {error}")
        return []


def validar_receta_ingrediente(id_receta, id_ingrediente):
    try:
        return RecetaIngrediente.select().where(
            (RecetaIngrediente.id_receta == id_receta) & (RecetaIngrediente.id_ingrediente == id_ingrediente)
        ).exists()
    except Exception as error:
        print(f"Error al validar ingrediente de receta: {error}")
        return False


def agregar_receta_ingrediente(id_receta, id_ingrediente, cantidad):
    if validar_receta_ingrediente(id_receta, id_ingrediente):
        print("Esa receta ya tiene asignado ese ingrediente.")
        return None
    try:
        return RecetaIngrediente.create(id_receta=id_receta, id_ingrediente=id_ingrediente, cantidad=cantidad)
    except Exception as error:
        print(f"Error al asignar ingrediente a la receta: {error}")
        return None


def actualizar_receta_ingrediente(id_receta, id_ingrediente, cantidad):
    try:
        filas = (RecetaIngrediente
            .update(cantidad=cantidad)
            .where((RecetaIngrediente.id_receta == id_receta) & (RecetaIngrediente.id_ingrediente == id_ingrediente))
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
            .where((RecetaIngrediente.id_receta == id_receta) & (RecetaIngrediente.id_ingrediente == id_ingrediente))
            .execute())
        if filas == 0:
            print("Esa receta no tiene asignado el ingrediente indicado.")
            return False
        return True
    except Exception as error:
        print(f"Error al eliminar ingrediente de la receta: {error}")
        return False
