# CREATE TABLE guardado (
#     id_guardado     INT PRIMARY KEY AUTO_INCREMENT,
#     id_usuario      INT NOT NULL,
#     id_receta       INT NOT NULL,
#     fecha_guardado  DATE NOT NULL DEFAULT (CURRENT_DATE),
#     FK usuario, FK receta, UNIQUE (id_usuario, id_receta)
# );
from peewee import AutoField, DateField, ForeignKeyField
from datos.modelos.base import base_model
from datos.modelos.usuario import usuario as Usuario
from datos.modelos.receta import Receta


class Guardado(base_model):
    id_guardado = AutoField()
    usuario = ForeignKeyField(Usuario, column_name='id_usuario', backref='guardados', on_delete='CASCADE')
    receta = ForeignKeyField(Receta, column_name='id_receta', backref='guardados', on_delete='CASCADE')
    fecha_guardado = DateField(null=False)

    class Meta:
        table_name = 'guardado'
        indexes = (
            (('usuario', 'receta'), True),
        )
