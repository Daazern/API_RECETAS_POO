#CREATE TABLE ingrediente (
#    id_ingrediente  INT PRIMARY KEY AUTO_INCREMENT,
#    nombre          VARCHAR(100) NOT NULL UNIQUE,
#    unidad_medida   VARCHAR(30) NOT NULL
#);

from peewee import Model, AutoField, CharField, DateField, IntegerField
from datos.sql.conexion import conectar

class base_model(Model):
    class Meta:
        database = conectar()

class Ingrediente(base_model):
    id_ingrediente = AutoField()
    nombre = CharField(max_length=100, unique=True)
    unidad_medida = CharField(max_length=30)

    class Meta:
        table_name = 'ingrediente'