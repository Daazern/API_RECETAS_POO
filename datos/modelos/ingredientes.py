#CREATE TABLE ingrediente (
#    id_ingrediente  INT PRIMARY KEY AUTO_INCREMENT,
#    nombre          VARCHAR(100) NOT NULL UNIQUE,
#    unidad_medida   VARCHAR(30) NOT NULL
#);

from datos.modelos.models import Ingrediente

__all__ = ["Ingrediente"]
