from peewee import Model, auto_field

from datos.sql.conexion import conectar

base_datos = conectar()

class BaseModel(Model):
    class Meta:
        database = base_datos

class pais(BaseModel):
    id_pais = auto_field()
    pais