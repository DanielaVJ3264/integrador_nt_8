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
# correo (texto)


#4. identifico los datos o el dato que sea un selector
ROLES=["ADMIN","EMPRESA","PARTICIPANTE"]

#5 defino mi DATASET
FILAS=400

#6. construyo una funcion para generar los N datos pedidos (LIMPIOS)
def generar_datos_limpios(numeros_datos=FILAS):
    filas=[]
    for _ in range(numeros_datos):

        filas.append({
            "id",
            "nombre",
            "correo",
            
        })
    