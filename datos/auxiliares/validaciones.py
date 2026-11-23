from decimal import Decimal, InvalidOperation


def a_entero(valor, campo="valor"):
    """Convierte a int. Si no es válido imprime el error y retorna None."""
    try:
        return int(str(valor).strip())
    except (ValueError, TypeError):
        print(f"Valor inválido en '{campo}': debe ser un número entero.")
        return None


def a_decimal(valor, campo="valor"):
    """Convierte a Decimal (acepta coma o punto). Si no es válido retorna None."""
    try:
        return Decimal(str(valor).strip().replace(",", "."))
    except (InvalidOperation, TypeError):
        print(f"Valor inválido en '{campo}': debe ser un número.")
        return None
