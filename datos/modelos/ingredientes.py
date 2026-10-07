from peewee import CharField, Model, auto_field

from datos.sql.conexion import conectar

db = conectar()

class BaseModel(Model):
    class Meta:
        database = db

class Ingrediente(BaseModel):
    id_ingrediente = auto_field()
    nombre = CharField(max_length=100, unique=True)
    unidad_medida = CharField(max_length=30)

    class Meta:
        table_name = "ingrediente"  