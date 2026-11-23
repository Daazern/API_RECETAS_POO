# CREATE TABLE receta_categoria (
#     id_receta       INT NOT NULL,
#     id_categoria    INT NOT NULL,
#     PRIMARY KEY (id_receta, id_categoria),
#     FK receta, FK categoria
# );
from peewee import ForeignKeyField, CompositeKey
from datos.modelos.base import base_model
from datos.modelos.receta import Receta
from datos.modelos.categoria import Categoria


class RecetaCategoria(base_model):
    receta = ForeignKeyField(Receta, column_name='id_receta', backref='categorias_rel', on_delete='CASCADE')
    categoria = ForeignKeyField(Categoria, column_name='id_categoria', backref='recetas_rel', on_delete='CASCADE')

    class Meta:
        table_name = 'receta_categoria'
        primary_key = CompositeKey('receta', 'categoria')
