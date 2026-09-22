"""
Tabla puente: vincula un Usuario con un Reto y deja trazabilidad. Crea el script `src/simular_registros.py`. Con la libreria **Faker** genera 800 filas falsas de la tabla `registros`, con las MISMAS columnas que usa Backend II. Despues **ensucia los datos a proposito**: nulos, duplicados, espacios sobrantes, mayusculas mezcladas y formatos distintos. Esos errores son los que vas a arreglar en la etapa de limpieza, asi que tienen que quedar bien puestos.

Usa `Faker("es_CO")` y fija la semilla con `Faker.seed(42)` y `random.seed(42)` para que el resultado sea SIEMPRE el mismo y tu compañero pueda reproducirlo.
"""
import random
import uuid
from faker import Faker

#1 configurar el faker a la region que necesito
fake=Faker("es_CO")

#2 Sembrar semillas para tener coherencia en los datos simulados


Faker.seed(42)
random.seed(42)

#3 Identifico los datos que deno simular
#id (texto (UUID))
# fecha_registro (fecha y hora)
# observacion (texto)
# estado (texto) selector!
# id_usuario (texto (UUID))
# id_reto (texto (UUID))

#4identifico los datos o el dato que sea un selector
ESTADO = ["PENDIENTE", "ACEPTADO", "RECHAZADO"]

#5 Defino mi DATASET
FILAS=800

#6Construyo una funcion para generrar los N datos pedidos (LIMPIOS)
def generar_datos_limpios(numero_datos=FILAS):
    filas = []
    for _ in range(numero_datos):
        filas.append({
            "id",
            "fecha_registro",
            "observacion",
            "estado",
            "id_usuario",
            "id_reto"
        })
