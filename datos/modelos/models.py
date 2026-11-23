from peewee import *
from datos.sql.conexion import conectar


defecto = "DEFAULT 0"
defecto_fecha = "DEFAULT (CURRENT_DATE)"

database = conectar()

class BaseModel(Model):
    class Meta:
        database = database

class Categoria(BaseModel):
    id_categoria = AutoField()
    nombre = CharField(max_length=100)
    tipo_comida = CharField(max_length=50)

    class Meta:
        table_name = 'categoria'

class Comentario(BaseModel):
    fecha = DateField(constraints=[SQL(defecto_fecha)])
    id_comentario = AutoField()
    id_receta = IntegerField(index=True)
    id_usuario = IntegerField(index=True)
    texto = TextField()

    class Meta:
        table_name = 'comentario'

class Guardado(BaseModel):
    fecha_guardado = DateField(constraints=[SQL(defecto_fecha)])
    id_guardado = AutoField()
    id_receta = IntegerField(index=True)
    id_usuario = IntegerField(index=True)

    class Meta:
        table_name = 'guardado'
        indexes = (
            (('id_usuario', 'id_receta'), True),
        )

class Ingrediente(BaseModel):
    id_ingrediente = AutoField()
    nombre = CharField(max_length=100, unique=True)
    unidad_medida = CharField(max_length=30)

    class Meta:
        table_name = 'ingrediente'

class Receta(BaseModel):
    descripcion = TextField(null=True)
    dificultad = CharField(max_length=20)
    fecha_publicacion = DateField(constraints=[SQL(defecto_fecha)])
    id_receta = AutoField()
    id_usuario = IntegerField(index=True)
    instrucciones = TextField()
    nombre = CharField(max_length=150)
    tiempo_preparacion = IntegerField()

    class Meta:
        table_name = 'receta'

class RecetaCategoria(BaseModel):
    id_categoria = IntegerField(index=True)
    id_receta = IntegerField(index=True)

    class Meta:
        table_name = 'receta_categoria'
        primary_key = CompositeKey('id_receta', 'id_categoria')

class RecetaIngrediente(BaseModel):
    cantidad = DecimalField(decimal_places=2, max_digits=10)
    id_ingrediente = IntegerField(index=True)
    id_receta = IntegerField(index=True)

    class Meta:
        table_name = 'receta_ingrediente'
        primary_key = CompositeKey('id_receta', 'id_ingrediente')

class Usuario(BaseModel):
    contrasena = CharField(max_length=255)
    email = CharField(max_length=150, unique=True)
    fecha_registro = DateField(constraints=[SQL(defecto_fecha)])
    id_usuario = AutoField()
    nombre = CharField(max_length=100)
    popularidad = IntegerField(constraints=[SQL(defecto)])
    rut = CharField(max_length=12, unique=True)

    class Meta:
        table_name = 'usuario'

class Valoracion(BaseModel):
    fecha = DateField(constraints=[SQL(defecto_fecha)])
    id_receta = IntegerField(index=True)
    id_usuario = IntegerField(index=True)
    id_valoracion = AutoField()
    puntuacion = IntegerField()

    class Meta:
        table_name = 'valoracion'
        indexes = (
            (('id_usuario', 'id_receta'), True),
        )
