import re

from datos.negocio.negocio_usuarios import (procesar_listado_usuarios, crear_usuario, actualizar_usuario_existente, eliminar_usuario_existente)
from datos.repositorios.repo_usuarios import (listar_usuarios,agregar_usuario,actualizar_usuario,eliminar_usuario,obtener_usuario_por_id)
# CREATE TABLE usuario (
#     id_usuario      INT PRIMARY KEY AUTO_INCREMENT,
#     nombre          VARCHAR(100) NOT NULL,
#     email           VARCHAR(150) NOT NULL UNIQUE,
#     contrasena      VARCHAR(255) NOT NULL,
#     fecha_registro  DATE NOT NULL DEFAULT (CURRENT_DATE),
#     popularidad      INT NOT NULL DEFAULT 0
# );
# alter table usuario add column rut varchar(12) not null unique;

while email=="":
    patron_correo = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    email = input("Ingrese el email del usuario: ")
    if not email:
        print("El email no puede estar vacío. Por favor, ingrese un valor válido.")
        email = ""

while contrasena=="":
    patron_contrasena = r"^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$"
    contrasena = input("Ingrese la contraseña del usuario: ")
    if not contrasena:
        print("La contraseña no puede estar vacía. Por favor, ingrese un valor válido.")
        contrasena = ""

while rut=="":
    patron_rut = r"^\d{1,2}\.\d{3}\.\d{3}-[\dkK]$"
    rut = input("Ingrese el RUT del usuario (formato: 12.345.678-9): ")
    if not rut:
        print("El RUT no puede estar vacío. Por favor, ingrese un valor válido.")
        rut = ""
    elif not re.fullmatch(patron_rut, rut):
        print("El RUT no tiene un formato válido.")
        rut = ""
    else:
        numero, digito_ingresado = rut.replace(".", "").split("-")
        suma = sum(int(digito) * peso for digito, peso in zip(reversed(numero), (2, 3, 4, 5, 6, 7) * 3))
        resultado = 11 - suma % 11
        digito_calculado = "0" if resultado == 11 else "K" if resultado == 10 else str(resultado)
        if digito_ingresado.upper() != digito_calculado:
            print("El dígito verificador del RUT no es válido.")
            rut = ""