# CREATE TABLE receta (
#     id_receta           INT PRIMARY KEY AUTO_INCREMENT,
#     id_usuario          INT NOT NULL,
#     nombre              VARCHAR(150) NOT NULL,
#     descripcion         TEXT,
#     tiempo_preparacion  INT NOT NULL,          -- en minutos
#     dificultad          VARCHAR(20) NOT NULL,  -- ej: 'facil','media','dificil'
#     instrucciones       TEXT NOT NULL,
#     fecha_publicacion   DATE NOT NULL DEFAULT (CURRENT_DATE),
#     CONSTRAINT fk_receta_usuario FOREIGN KEY (id_usuario) REFERENCES usuario(id_usuario) ON DELETE CASCADE
# );
from peewee import AutoField, CharField, TextField, IntegerField, DateField, ForeignKeyField
from datos.modelos.base import base_model
from datos.modelos.usuario import usuario as Usuario


class Receta(base_model):
    id_receta = AutoField()
    usuario = ForeignKeyField(Usuario, column_name='id_usuario', backref='recetas', on_delete='CASCADE')
    nombre = CharField(max_length=150, null=False)
    descripcion = TextField(null=True)
    tiempo_preparacion = IntegerField(null=False)
    dificultad = CharField(max_length=20, null=False)
    instrucciones = TextField(null=False)
    fecha_publicacion = DateField(null=False)

    class Meta:
        table_name = 'receta'
