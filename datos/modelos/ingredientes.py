from peewee import AutoField, CharField, Model

from datos.sql.conexion import conectar

db = conectar()

class BaseModel(Model):
    class Meta:
        database = db

class Ingrediente(BaseModel):
    id_ingrediente = AutoField()
    nombre = CharField(max_length=100, unique=True)
    unidad_medida = CharField(max_length=30)

    class Meta:
        table_name = "ingrediente"  