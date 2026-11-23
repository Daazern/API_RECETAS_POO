from peewee import Model
from datos.sql.conexion import conectar

database = conectar()


class base_model(Model):
    class Meta:
        database = database
