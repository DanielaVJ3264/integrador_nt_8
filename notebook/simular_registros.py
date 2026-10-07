"""
Tabla puente: vincula un Usuario con un Reto y deja trazabilidad. Crea el script `src/simular_registros.py`. Con la libreria **Faker** genera 800 filas falsas de la tabla `registros`, con las MISMAS columnas que usa Backend II. Despues **ensucia los datos a proposito**: nulos, duplicados, espacios sobrantes, mayusculas mezcladas y formatos distintos. Esos errores son los que vas a arreglar en la etapa de limpieza, asi que tienen que quedar bien puestos.

Usa `Faker("es_CO")` y fija la semilla con `Faker.seed(42)` y `random.seed(42)` para que el resultado sea SIEMPRE el mismo y tu compañero pueda reproducirlo.
"""
import random
import uuid
import pandas as pd
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
# estado (texto)
# id_usuario (texto (UUID))
# id_reto (texto (UUID))

#4identifico los datos o el dato que sea un selector
ESTADO = ["PENDIENTE", "ACEPTADO", "RECHAZADO", "EN_PROCESO", "FINALIZADO"]
IDS_USUARIOS = IDS_USUARIOS = [
    "usuario1",
    "usuario2",
    "usuario3",
    "usuario4",
    "usuario5"
]
IDS_RETOS = [
    "reto1",
    "reto2",
    "reto3",
    "reto4",
    "reto5"
]

#5 Defino mi DATASET
FILAS=800

#6Construyo una funcion para generrar los N datos pedidos (LIMPIOS)
def generar_datos_limpios(numero_datos=FILAS):
    filas = []
    for _ in range(numero_datos):
        filas.append({
            "id":str(uuid.uuid4()),
            "fecha_registro":fake.date_time_between(start_date='-1y', end_date='now'),
            "observacion":fake.sentence(nb_words=10),
            "estado":random.choice(ESTADO),
            "id_usuario":random.choice(IDS_USUARIOS),
            "id_reto":random.choice(IDS_RETOS)
        })
    return filas
variable_dia=pd.DataFrame(generar_datos_limpios())


#Ensuciar los datos 


    #1. crear una funcion para definir porcentajes de error
def generar_muestra(datos,porcentaje):
        return datos.sample(fraccion=porcentaje, random_state=random.randint(0,999)).index

    #2. crear una funcion para escribir mal un texto
def escribir_mal(texto):
        variantes=[texto.lower(),f" {texto.title()} ", texto.capitalize()]
        return random.choice(variantes)

    #3. crear una funcion para convertir booleanos en textos
def convertir_booleano_texto(valor):
        if valor:
            return random.choice(["SI", "1"])
        return random.choice(["NO", "0"])
#4 Funcion para ensuciar datos
def ensuciar(datos_df):
        datos_df=datos_df.copy()

        filas_elegidas=generar_muestra(datos_df,0.10)

        #fecha formatos mezclados
        
        iso=datos_df["fecha_registro"].dt.strftime("%Y-%m-%d %H:%M:%S")
        latino=datos_df["fecha_registro"].dt.strftime("%d/%m/%Y %H:%M")
        datos_df["fecha_registro"] = iso
        filas_elegidas = generar_muestra(datos_df, 0.40)
        datos_df.loc[filas_elegidas, "fecha_registro"] = latino.loc[filas_elegidas]

        #Se ensucia `observacion`: 20% en None (nulos).

        filas_elegidas = generar_muestra(datos_df, 0.20)
        datos_df.loc[filas_elegidas, "observacion"] = None

        #Se ensucia `estado`: variantes: 'inscrito', 'EN PROCESO', ' Finalizado '.
        filas_elegidas = generar_muestra(datos_df, 0.10)
        datos_df.loc[filas_elegidas, "estado"] = datos_df.loc[filas_elegidas, "estado"].map(escribir_mal)

        #10% con el par `id_usuario` + `id_reto` REPETIDO: el mismo usuario inscrito dos veces en el mismo reto (eso el back lo prohibe con 409).
        filas_elegidas = generar_muestra(datos_df, 0.10)
        datos_df.loc[filas_elegidas, ["id_usuario", "id_reto"]] = datos_df.loc[filas_elegidas, ["id_usuario", "id_reto"]].sample(frac=1).values

        #5% de las filas repetidas tal cual (duplicados exactos).
        filas_elegidas = generar_muestra(datos_df, 0.05)
        datos_df = pd.concat([datos_df, datos_df.loc[filas_elegidas]], ignore_index=True)
        
