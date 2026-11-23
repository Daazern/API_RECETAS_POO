# CREATE TABLE valoracion (
#     id_valoracion   INT PRIMARY KEY AUTO_INCREMENT,
#     id_usuario      INT NOT NULL,
#     id_receta       INT NOT NULL,
#     puntuacion      INT NOT NULL CHECK (puntuacion BETWEEN 1 AND 5),
#     fecha           DATE NOT NULL DEFAULT (CURRENT_DATE),
#     FK usuario, FK receta, UNIQUE (id_usuario, id_receta)
# );
from peewee import AutoField, IntegerField, DateField, ForeignKeyField
from datos.modelos.base import base_model
from datos.modelos.usuario import usuario as Usuario
from datos.modelos.receta import Receta


class Valoracion(base_model):
    id_valoracion = AutoField()
    usuario = ForeignKeyField(Usuario, column_name='id_usuario', backref='valoraciones', on_delete='CASCADE')
    receta = ForeignKeyField(Receta, column_name='id_receta', backref='valoraciones', on_delete='CASCADE')
    puntuacion = IntegerField(null=False)
    fecha = DateField(null=False)

    class Meta:
        table_name = 'valoracion'
        indexes = (
            (('usuario', 'receta'), True),
        )
