'''
Organizacion que registra o propone retos. Crea el script `src/simular_empresas.py`. 
Con la libreria **Faker** genera 300 filas falsas de la tabla `empresas`, con las MISMAS columnas que usa Backend II. 
Despues **ensucia los datos a proposito**: nulos, duplicados, espacios sobrantes, mayusculas mezcladas y formatos distintos. 
Esos errores son los que vas a arreglar en la etapa de limpieza, asi que tienen que quedar bien puestos.

Usa `Faker("es_CO")` y fija la semilla con `Faker.seed(42)` y `random.seed(42)` para que el resultado sea SIEMPRE el mismo y tu compañero pueda reproducirlo.

'''
import random
import uuid
from faker import Faker

#1. configurar el faker a la region que necesito
fake=Faker("es_CO")

#2. fijar la semilla para que el resultado sea siempre el mismo
Faker.seed(42)
random.seed(42)

#3. identifico los datos que debo simular
#id (texto (UUID))
# nombre (texto)
# nit (texto)
# sector (texto) seleccionable por el usuario
# contacto (texto)
# correo (texto)
# telefono (texto)
# activa (booleano)

#4. identifico los datos o el dato que sea un selector
ROLES=["TECNOLOGIAS","SALUD","ALIMENTOS"]

#5 defino mi DATASET
FILAS=300

#6. construyo una funcion para generar los N datos pedidos (LIMPIOS)
def generar_datos_limpios(numeros_datos=FILAS):
    filas=[]
    for _ in range(numeros_datos):

        filas.append({
            "id",
            "nombre",
            "nit",
            "sector",
            "contacto",
            "correo",
            "telefono",
            "activa"
        })

