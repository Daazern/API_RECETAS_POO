create database if not exists api_recetas;

use api_recetas;

CREATE TABLE usuario (
    id_usuario      INT PRIMARY KEY AUTO_INCREMENT,
    nombre          VARCHAR(100) NOT NULL,
    email           VARCHAR(150) NOT NULL UNIQUE,
    contrasena      VARCHAR(255) NOT NULL,
    fecha_registro  DATE NOT NULL DEFAULT (CURRENT_DATE)
);

CREATE TABLE receta (
    id_receta           INT PRIMARY KEY AUTO_INCREMENT,
    id_usuario          INT NOT NULL,
    nombre              VARCHAR(150) NOT NULL,
    descripcion         TEXT,
    tiempo_preparacion  INT NOT NULL,          -- en minutos
    dificultad          VARCHAR(20) NOT NULL,  -- ej: 'facil','media','dificil'
    instrucciones       TEXT NOT NULL,
    fecha_publicacion   DATE NOT NULL DEFAULT (CURRENT_DATE),
    CONSTRAINT fk_receta_usuario
        FOREIGN KEY (id_usuario) REFERENCES usuario(id_usuario)
        ON DELETE CASCADE
);

CREATE TABLE ingrediente (
    id_ingrediente  INT PRIMARY KEY AUTO_INCREMENT,
    nombre          VARCHAR(100) NOT NULL UNIQUE,
    unidad_medida   VARCHAR(30) NOT NULL
);


CREATE TABLE categoria (
    id_categoria    INT PRIMARY KEY AUTO_INCREMENT,
    nombre          VARCHAR(100) NOT NULL,
    tipo_comida     VARCHAR(50)  NOT NULL
);


CREATE TABLE comentario (
    id_comentario   INT PRIMARY KEY AUTO_INCREMENT,
    id_usuario      INT NOT NULL,
    id_receta       INT NOT NULL,
    texto           TEXT NOT NULL,
    fecha           DATE NOT NULL DEFAULT (CURRENT_DATE),
    CONSTRAINT fk_comentario_usuario
        FOREIGN KEY (id_usuario) REFERENCES usuario(id_usuario)
        ON DELETE CASCADE,
    CONSTRAINT fk_comentario_receta
        FOREIGN KEY (id_receta) REFERENCES receta(id_receta)
        ON DELETE CASCADE
);

CREATE TABLE valoracion (
    id_valoracion   INT PRIMARY KEY AUTO_INCREMENT,
    id_usuario      INT NOT NULL,
    id_receta       INT NOT NULL,
    puntuacion      INT NOT NULL CHECK (puntuacion BETWEEN 1 AND 5),
    fecha           DATE NOT NULL DEFAULT (CURRENT_DATE),
    CONSTRAINT fk_valoracion_usuario
        FOREIGN KEY (id_usuario) REFERENCES usuario(id_usuario)
        ON DELETE CASCADE,
    CONSTRAINT fk_valoracion_receta
        FOREIGN KEY (id_receta) REFERENCES receta(id_receta)
        ON DELETE CASCADE,
    CONSTRAINT uq_valoracion_usuario_receta
        UNIQUE (id_usuario, id_receta)
);

CREATE TABLE guardado (
    id_guardado     INT PRIMARY KEY AUTO_INCREMENT,
    id_usuario      INT NOT NULL,
    id_receta       INT NOT NULL,
    fecha_guardado  DATE NOT NULL DEFAULT (CURRENT_DATE),
    CONSTRAINT fk_guardado_usuario
        FOREIGN KEY (id_usuario) REFERENCES usuario(id_usuario)
        ON DELETE CASCADE,
    CONSTRAINT fk_guardado_receta
        FOREIGN KEY (id_receta) REFERENCES receta(id_receta)
        ON DELETE CASCADE,
    CONSTRAINT uq_guardado_usuario_receta
        UNIQUE (id_usuario, id_receta)
);

CREATE TABLE receta_categoria (
    id_receta       INT NOT NULL,
    id_categoria    INT NOT NULL,
    PRIMARY KEY (id_receta, id_categoria),
    CONSTRAINT fk_recetacategoria_receta
        FOREIGN KEY (id_receta) REFERENCES receta(id_receta)
        ON DELETE CASCADE,
    CONSTRAINT fk_recetacategoria_categoria
        FOREIGN KEY (id_categoria) REFERENCES categoria(id_categoria)
        ON DELETE CASCADE
);

CREATE TABLE receta_ingrediente (
    id_receta       INT NOT NULL,
    id_ingrediente  INT NOT NULL,
    cantidad        DECIMAL(10,2) NOT NULL,
    PRIMARY KEY (id_receta, id_ingrediente),
    CONSTRAINT fk_recetaingrediente_receta
        FOREIGN KEY (id_receta) REFERENCES receta(id_receta)
        ON DELETE CASCADE,
    CONSTRAINT fk_recetaingrediente_ingrediente
        FOREIGN KEY (id_ingrediente) REFERENCES ingrediente(id_ingrediente)
        ON DELETE CASCADE
);