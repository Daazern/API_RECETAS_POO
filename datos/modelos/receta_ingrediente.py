# CREATE TABLE receta_ingrediente (
#     id_receta       INT NOT NULL,
#     id_ingrediente  INT NOT NULL,
#     cantidad        DECIMAL(10,2) NOT NULL,
#     PRIMARY KEY (id_receta, id_ingrediente),
#     FK receta, FK ingrediente
# );
from peewee import ForeignKeyField, CompositeKey, DecimalField
from datos.modelos.base import base_model
from datos.modelos.receta import Receta
from datos.modelos.ingredientes import Ingrediente


class RecetaIngrediente(base_model):
    receta = ForeignKeyField(Receta, column_name='id_receta', backref='ingredientes_rel', on_delete='CASCADE')
    ingrediente = ForeignKeyField(Ingrediente, column_name='id_ingrediente', backref='recetas_rel', on_delete='CASCADE')
    cantidad = DecimalField(max_digits=10, decimal_places=2, null=False)

    class Meta:
        table_name = 'receta_ingrediente'
        primary_key = CompositeKey('receta', 'ingrediente')
