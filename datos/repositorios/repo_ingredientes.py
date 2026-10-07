from datos.modelos.ingredientes import Ingredientes

def listar_ingredientes():
    ingredientes = Ingredientes.select()
    if ingredientes:
        return ingredientes