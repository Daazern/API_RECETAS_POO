from datos.modelos.categoria import Categoria


def listar_categorias():
    try:
        return list(Categoria.select().order_by(Categoria.id_categoria))
    except Exception as error:
        print(f"Error al listar categorías: {error}")
        return []


def obtener_categoria_por_id(id_categoria):
    try:
        return Categoria.get_by_id(id_categoria)
    except Categoria.DoesNotExist:
        print(f"Categoría con ID {id_categoria} no encontrada.")
        return None
    except Exception as error:
        print(f"Error al obtener categoría: {error}")
        return None


def agregar_categoria(nombre, tipo_comida):
    try:
        return Categoria.create(nombre=nombre, tipo_comida=tipo_comida)
    except Exception as error:
        print(f"Error al agregar categoría: {error}")
        return None


def actualizar_categoria(id_categoria, nombre, tipo_comida):
    try:
        categoria = Categoria.get_by_id(id_categoria)
        categoria.nombre = nombre
        categoria.tipo_comida = tipo_comida
        categoria.save()
        return categoria
    except Categoria.DoesNotExist:
        print(f"Categoría con ID {id_categoria} no encontrada.")
        return None
    except Exception as error:
        print(f"Error al actualizar categoría: {error}")
        return None


def eliminar_categoria(id_categoria):
    try:
        categoria = Categoria.get_by_id(id_categoria)
        categoria.delete_instance()
        return True
    except Categoria.DoesNotExist:
        print(f"Categoría con ID {id_categoria} no encontrada.")
        return False
    except Exception as error:
        print(f"Error al eliminar categoría: {error}")
        return False
