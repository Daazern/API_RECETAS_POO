# CREATE TABLE usuario (
#     id_usuario      INT PRIMARY KEY AUTO_INCREMENT,
#     nombre          VARCHAR(100) NOT NULL,
#     email           VARCHAR(150) NOT NULL UNIQUE,
#     contrasena      VARCHAR(255) NOT NULL,
#     fecha_registro  DATE NOT NULL DEFAULT (CURRENT_DATE),
#     popularidad      INT NOT NULL DEFAULT 0
# );
from peewee import Model, AutoField, CharField, DateField, IntegerField
from datos.sql.conexion import conectar

class base_model(Model):
    class Meta:
        database = conectar()

class usuario(base_model):
    id_usuario = AutoField()
    nombre = CharField(max_length=100, null=False)
    email = CharField(max_length=150, unique=True, null=False)
    contrasena = CharField(max_length=255, null=False)
    fecha_registro = DateField(null=False)
    popularidad = IntegerField(default=0, null=False)

    class Meta:
        table_name = 'usuario'

