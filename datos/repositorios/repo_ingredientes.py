from datos.modelos.ingredientes import Ingrediente


def listar_ingredientes():
    try:
        return list(Ingrediente.select().order_by(Ingrediente.id_ingrediente))
    except Exception as error:
        print(f"Error al listar ingredientes: {error}")
        return []


def agregar_ingrediente(nombre, unidad_medida):
    """Crea el ingrediente si no existe (nombre es UNIQUE). Devuelve el ingrediente o None."""
    try:
        ingrediente, _creado = Ingrediente.get_or_create(
            nombre=nombre,
            defaults={"unidad_medida": unidad_medida},
        )
        return ingrediente
    except Exception as error:
        print(f"Error al agregar ingrediente: {error}")
        return None
