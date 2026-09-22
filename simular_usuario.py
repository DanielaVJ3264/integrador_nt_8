import random
import uuid
from faker import Faker

#1 configurar el faker a la region que necesito
fake=Faker("es_CO")

#2 Sembrar semillas para tener coherencia en los datos simulados


Faker.seed(42)
random.seed(42)

#3 Identifico los datos que deno simular
#id(texto(UUID))
#nombre(texto)
#correo(texto)

#4identifico los datos o el dato que sea un selector
ROLES = ["ADMIN", "EMPRESA", "PARTICIPANTE"]

#5 Defino mi DATASET
FILAS=400

#6Construyo una funcion para generrar los N datos pedidos (LIMPIOS)
def generar_datos_limpios(numero_datos=FILAS):
    filas = []
    for _ in range(numero_datos):
        filas.append({
            "id",
            "nombre",
            "correo",


        })