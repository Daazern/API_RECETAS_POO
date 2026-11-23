from datos.modelos.models import RecetaCategoria, Receta, Categoria


def listar_receta_categorias():
    try:
        return list(
            RecetaCategoria.select(RecetaCategoria, Receta, Categoria)
            .join(Receta, on=(RecetaCategoria.id_receta == Receta.id_receta), attr='receta')
            .switch(RecetaCategoria)
            .join(Categoria, on=(RecetaCategoria.id_categoria == Categoria.id_categoria), attr='categoria')
            .order_by(RecetaCategoria.id_receta, RecetaCategoria.id_categoria)
        )
    except Exception as error:
        print(f"Error al listar categorías de recetas: {error}")
        return []


def validar_receta_categoria(id_receta, id_categoria):
    try:
        return RecetaCategoria.select().where(
            (RecetaCategoria.id_receta == id_receta) & (RecetaCategoria.id_categoria == id_categoria)
        ).exists()
    except Exception as error:
        print(f"Error al validar categoría de receta: {error}")
        return False


def agregar_receta_categoria(id_receta, id_categoria):
    if validar_receta_categoria(id_receta, id_categoria):
        print("Esa receta ya tiene asignada esa categoría.")
        return None
    try:
        return RecetaCategoria.create(id_receta=id_receta, id_categoria=id_categoria)
    except Exception as error:
        print(f"Error al asignar categoría a la receta: {error}")
        return None


def actualizar_receta_categoria(id_receta, id_categoria_actual, id_categoria_nueva):
    if not validar_receta_categoria(id_receta, id_categoria_actual):
        print("Esa receta no tiene asignada la categoría indicada.")
        return False
    if validar_receta_categoria(id_receta, id_categoria_nueva):
        print("Esa receta ya tiene asignada la categoría nueva.")
        return False
    try:
        (RecetaCategoria
            .update(id_categoria=id_categoria_nueva)
            .where((RecetaCategoria.id_receta == id_receta) & (RecetaCategoria.id_categoria == id_categoria_actual))
            .execute())
        return True
    except Exception as error:
        print(f"Error al actualizar categoría de la receta: {error}")
        return False


def eliminar_receta_categoria(id_receta, id_categoria):
    try:
        filas = (RecetaCategoria
            .delete()
            .where((RecetaCategoria.id_receta == id_receta) & (RecetaCategoria.id_categoria == id_categoria))
            .execute())
        if filas == 0:
            print("Esa receta no tiene asignada la categoría indicada.")
            return False
        return True
    except Exception as error:
        print(f"Error al eliminar categoría de la receta: {error}")
        return False
