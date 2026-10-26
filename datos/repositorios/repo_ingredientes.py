from datos.modelos.ingredientes import Ingrediente


def listar_ingredientes():
    try:
        return list(Ingrediente.select().order_by(Ingrediente.id_ingrediente))
    except Exception as error:
        print(f"Error al listar ingredientes: {error}")
        return []


def agregar_ingrediente(nombre, unidad_medida):
    try:
        ingrediente, _creado = Ingrediente.get_or_create(
            nombre=nombre,
            defaults={"unidad_medida": unidad_medida},
        )
        return ingrediente
    except Exception as error:
        print(f"Error al agregar ingrediente: {error}")
        return None

def actualizar_ingrediente(id_ingrediente, nombre, unidad_medida):
    try:
        ingrediente = Ingrediente.get_by_id(id_ingrediente)
        ingrediente.nombre = nombre
        ingrediente.unidad_medida = unidad_medida
        ingrediente.save()
        return ingrediente
    except Ingrediente.DoesNotExist:
        print(f"Ingrediente con ID {id_ingrediente} no encontrado.")
        return None
    except Exception as error:
        print(f"Error al actualizar ingrediente: {error}")
        return None

def eliminar_ingrediente(id_ingrediente):
    try:
        ingrediente = Ingrediente.get_by_id(id_ingrediente)
        ingrediente.delete_instance()
        return True
    except Ingrediente.DoesNotExist:
        print(f"Ingrediente con ID {id_ingrediente} no encontrado.")
        return False
    except Exception as error:
        print(f"Error al eliminar ingrediente: {error}")
        return False