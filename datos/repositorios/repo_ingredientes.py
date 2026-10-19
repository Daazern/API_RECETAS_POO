from datos.modelos.ingredientes import Ingredientes

def listar_ingredientes():
    try:
        ingredientes = Ingredientes.select()
        return ingredientes 
    except Exception as error:
        print(f"Error al listar ingredientes: {error}")
        return []

def agregar_ingrediente(nombre, cantidad):
    try:
        ingrediente = Ingredientes.create(nombre=nombre, cantidad=cantidad)
        return ingrediente
    except Exception as error:
        print(f"Error al agregar ingrediente: {error}")
        return None