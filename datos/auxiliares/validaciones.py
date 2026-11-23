import re
from decimal import Decimal, InvalidOperation

import bcrypt


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


# ---------- Validaciones de usuario ----------

PATRON_EMAIL = r"^[\w\.-]+@[\w\.-]+\.\w+$"
PATRON_CONTRASENA = r"^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$"
MENSAJE_CONTRASENA = (
    "La contraseña debe tener al menos 8 caracteres, e incluir una mayúscula, "
    "una minúscula, un número y un símbolo (#?!@$%^&*-)."
)


def validar_formato_email(email):
    """Retorna el email normalizado o None (imprime el motivo)."""
    email = (email or "").strip()
    if not email:
        print("El email no puede estar vacío.")
        return None
    if len(email) > 150 or not re.fullmatch(PATRON_EMAIL, email):
        print("El email no tiene un formato válido.")
        return None
    return email


def validar_formato_contrasena(contrasena):
    """Retorna True si la contraseña cumple las reglas; si no, imprime el motivo."""
    if not contrasena:
        print("La contraseña no puede estar vacía.")
        return False
    if not re.fullmatch(PATRON_CONTRASENA, contrasena):
        print(MENSAJE_CONTRASENA)
        return False
    if len(contrasena.encode("utf-8")) > 72:  # límite de bcrypt
        print("La contraseña no puede superar los 72 bytes.")
        return False
    return True


def validar_rut(rut):
    """Solicita obligatoriamente un RUT válido y retorna su formato normalizado (12.345.678-9)."""
    while True:
        rut = rut or input("Ingrese el RUT (ej: 12.345.678-9): ")
        rut = rut.strip().replace(".", "").upper()

        if not rut:
            print("El RUT no puede estar vacío.")
            rut = None
            continue
        if not re.fullmatch(r"\d{7,8}-[\dK]", rut):
            print("El RUT no tiene un formato válido (ej: 12.345.678-9).")
            rut = None
            continue

        numero, digito = rut.split("-")
        suma = sum(int(d) * peso for d, peso in zip(reversed(numero), (2, 3, 4, 5, 6, 7) * 2))
        resultado = 11 - suma % 11

        if resultado == 11:
            esperado = "0"
        elif resultado == 10:
            esperado = "K"
        else:
            esperado = str(resultado)

        if digito != esperado:
            print("El dígito verificador del RUT no es válido.")
            rut = None
            continue

        return f"{int(numero):,}".replace(",", ".") + "-" + digito


# ---------- Cifrado de contraseñas (bcrypt) ----------

def encriptar_contrasena(contrasena):
    """Retorna el hash bcrypt (str, 60 caracteres) de la contraseña."""
    return bcrypt.hashpw(contrasena.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")


def verificar_contrasena(contrasena, hash_guardado):
    """True si la contraseña en texto plano corresponde al hash guardado."""
    try:
        return bcrypt.checkpw(contrasena.encode("utf-8"), hash_guardado.encode("utf-8"))
    except (ValueError, AttributeError):
        return False
