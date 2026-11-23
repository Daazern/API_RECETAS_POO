# CREATE TABLE comentario (
#     id_comentario   INT PRIMARY KEY AUTO_INCREMENT,
#     id_usuario      INT NOT NULL,
#     id_receta       INT NOT NULL,
#     texto           TEXT NOT NULL,
#     fecha           DATE NOT NULL DEFAULT (CURRENT_DATE),
#     FK usuario ON DELETE CASCADE, FK receta ON DELETE CASCADE
# );
from peewee import AutoField, TextField, DateField, ForeignKeyField
from datos.modelos.base import base_model
from datos.modelos.usuario import usuario as Usuario
from datos.modelos.receta import Receta


class Comentario(base_model):
    id_comentario = AutoField()
    usuario = ForeignKeyField(Usuario, column_name='id_usuario', backref='comentarios', on_delete='CASCADE')
    receta = ForeignKeyField(Receta, column_name='id_receta', backref='comentarios', on_delete='CASCADE')
    texto = TextField(null=False)
    fecha = DateField(null=False)

    class Meta:
        table_name = 'comentario'
