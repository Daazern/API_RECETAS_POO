import prettytable

from datos.negocio.negocio_ingredientes import (
    procesar_listado_ingredientes,
    procesar_nuevo_ingrediente,
)
from datos.presentacion.menu import cargar_menu


def main():
    cargar_menu()

    print("\nIngredientes actuales:")
    print(procesar_listado_ingredientes(prettytable.PrettyTable()))

    procesar_nuevo_ingrediente("Tomate", "Unidad")

    print("\nIngredientes después de agregar:")
    print(procesar_listado_ingredientes(prettytable.PrettyTable()))


if __name__ == "__main__":
    main()
