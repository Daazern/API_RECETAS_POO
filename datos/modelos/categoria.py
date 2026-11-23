# CREATE TABLE categoria (
#     id_categoria    INT PRIMARY KEY AUTO_INCREMENT,
#     nombre          VARCHAR(100) NOT NULL,
#     tipo_comida     VARCHAR(50)  NOT NULL
# );
from peewee import AutoField, CharField
from datos.modelos.base import base_model


class Categoria(base_model):
    id_categoria = AutoField()
    nombre = CharField(max_length=100, null=False)
    tipo_comida = CharField(max_length=50, null=False)

    class Meta:
        table_name = 'categoria'
