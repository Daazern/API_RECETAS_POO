from peewee import (
    AutoField, CharField, TextField, IntegerField, DecimalField, DateField,
    ForeignKeyField, CompositeKey, Model, SQL,
)

from datos.sql.conexion import conectar

database = conectar()


class BaseModel(Model):
    class Meta:
        database = database


class Usuario(BaseModel):
    id_usuario = AutoField()
    nombre = CharField(max_length=100)
    email = CharField(max_length=150, unique=True)
    contrasena = CharField(max_length=255)
    fecha_registro = DateField(constraints=[SQL("DEFAULT (CURRENT_DATE)")])
    popularidad = IntegerField(constraints=[SQL("DEFAULT 0")])

    class Meta:
        table_name = 'usuario'


class Receta(BaseModel):
    id_receta = AutoField()
    usuario = ForeignKeyField(
        Usuario, column_name='id_usuario',
        backref='recetas', on_delete='CASCADE',
    )
    nombre = CharField(max_length=150)
    descripcion = TextField(null=True)
    tiempo_preparacion = IntegerField()               # minutos
    dificultad = CharField(max_length=20)             # facil, media, dificil
    instrucciones = TextField()
    fecha_publicacion = DateField(constraints=[SQL("DEFAULT (CURRENT_DATE)")])

    class Meta:
        table_name = 'receta'


class Ingrediente(BaseModel):
    id_ingrediente = AutoField()
    nombre = CharField(max_length=100, unique=True)
    unidad_medida = CharField(max_length=30)

    class Meta:
        table_name = 'ingrediente'


class Categoria(BaseModel):
    id_categoria = AutoField()
    nombre = CharField(max_length=100)
    tipo_comida = CharField(max_length=50)

    class Meta:
        table_name = 'categoria'


class Comentario(BaseModel):
    id_comentario = AutoField()
    usuario = ForeignKeyField(
        Usuario, column_name='id_usuario',
        backref='comentarios', on_delete='CASCADE',
    )
    receta = ForeignKeyField(
        Receta, column_name='id_receta',
        backref='comentarios', on_delete='CASCADE',
    )
    texto = TextField()
    fecha = DateField(constraints=[SQL("DEFAULT (CURRENT_DATE)")])

    class Meta:
        table_name = 'comentario'


class Valoracion(BaseModel):
    id_valoracion = AutoField()
    usuario = ForeignKeyField(
        Usuario, column_name='id_usuario',
        backref='valoraciones', on_delete='CASCADE',
    )
    receta = ForeignKeyField(
        Receta, column_name='id_receta',
        backref='valoraciones', on_delete='CASCADE',
    )
    puntuacion = IntegerField()                       # 1 a 5 (CHECK en la BD)
    fecha = DateField(constraints=[SQL("DEFAULT (CURRENT_DATE)")])

    class Meta:
        table_name = 'valoracion'
        indexes = (
            (('usuario', 'receta'), True),            # UNIQUE (id_usuario, id_receta)
        )


class Guardado(BaseModel):
    id_guardado = AutoField()
    usuario = ForeignKeyField(
        Usuario, column_name='id_usuario',
        backref='guardados', on_delete='CASCADE',
    )
    receta = ForeignKeyField(
        Receta, column_name='id_receta',
        backref='guardados', on_delete='CASCADE',
    )
    fecha_guardado = DateField(constraints=[SQL("DEFAULT (CURRENT_DATE)")])

    class Meta:
        table_name = 'guardado'
        indexes = (
            (('usuario', 'receta'), True),
        )


class RecetaCategoria(BaseModel):
    receta = ForeignKeyField(
        Receta, column_name='id_receta',
        backref='categorias_rel', on_delete='CASCADE',
    )
    categoria = ForeignKeyField(
        Categoria, column_name='id_categoria',
        backref='recetas_rel', on_delete='CASCADE',
    )

    class Meta:
        table_name = 'receta_categoria'
        primary_key = CompositeKey('receta', 'categoria')


class RecetaIngrediente(BaseModel):
    receta = ForeignKeyField(
        Receta, column_name='id_receta',
        backref='ingredientes_rel', on_delete='CASCADE',
    )
    ingrediente = ForeignKeyField(
        Ingrediente, column_name='id_ingrediente',
        backref='recetas_rel', on_delete='CASCADE',
    )
    cantidad = DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        table_name = 'receta_ingrediente'
        primary_key = CompositeKey('receta', 'ingrediente')
