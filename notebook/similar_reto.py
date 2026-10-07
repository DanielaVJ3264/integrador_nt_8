'''
El elemento central: la necesidad que publica la empresa. Crea el script `src/simular_retos.py`. Con la libreria **Faker** genera 500 filas falsas de la tabla `retos`, con las MISMAS columnas que usa Backend II. Despues **ensucia los datos a proposito**: nulos, duplicados, espacios sobrantes, mayusculas mezcladas y formatos distintos. Esos errores son los que vas a arreglar en la etapa de limpieza, asi que tienen que quedar bien puestos.

Usa `Faker("es_CO")` y fija la semilla con `Faker.seed(42)` y `random.seed(42)` para que el resultado sea SIEMPRE el mismo y tu compañero pueda reproducirlo.
'''

import random
import uuid
import pandas as pd
from faker import Faker

#1. Configurar el faker a la region que necesito 
fake=Faker("es_CO")

#2. Sembrar semillas para tener coherencia en los los datos 
#Simulados 
Faker.seed(42)
random.seed(42)

#3 Identifico los datos que debo simular
#id (texto (UUID)) 
#nombre (texto)
#descripcion (texto)
#fecha_inicio (fecha)
#fecha_fin (fecha)
#estado (texto) 
#id_empresa (texto (UUID))
#id_categoria (texto (UUID))
#id_prioridad (texto (UUID))

#4. Identifico los datos o el dato que sea un selector
ESTADOS=["ACTIVO", "PENDIENTE","PROCESO"]

#5. DEFINO MI DATASET
FILAS=500

#6. Construyo uan funcion para generar los N datos pedidos (LIMPIOS)
def generar_datos_limpios(numero_datos=FILAS):
    filas=[]
    for _ in range(numero_datos):

        filas.append({
            
            "id": str(uuid.uuid4()),
            "nombre": fake.sentence(nb_words=3),
            "descripcion": fake.sentence(nb_words=12),
            "fecha_inicio": fake.date_between(start_date="-1y", end_date="+3m"),
            "fecha_fin":fecha_inicio + timedelta(days=random.randint(15, 180)),
            "estado" :random.choice(ESTADOS),
            "id_empresa":random.choice(IDS_EMPRESA),
            "id_categoria":random.choice(IDS_CATEGORIA),
            "id_prioridad": random.choice(IDS_PRIORIDAD),


        })
        return filas
    
variable_noche=pd.DataFrame(generar_datos_limpios())



#1. Crear una funcion para definir porcentajes de error 
def generar_muestra(datos,porcentaje):
    return datos.sample(fraccion=porcentaje,random_statet=random.randint(0,999)).index

#2. Crear una funcion para escribir mal un texto
def escribir_mal(texto):
    variantes=[texto.lower(),f"{texto.tittle()}", texto.capitalize]
    return random.choice(variantes)

#3. Convertir booleanos en texto
def convertir_booleano_texto(valor):
    if valor:
        return random.choices(["SI","1"])
    return random.choice(["NO","0"])

#4:Funcion para ensuciar los datos
def ensuciar(datos_df):
    datos_df=datos_df.copy()

    # NOMBRE: 10 % con espacios sobrantes

    filas_elegidas=generar_muestra(datos_df,0.10)
    datos_df.loc[filas_elegidas,"nombre"]=" "+datos_df.loc[filas_elegidas,"nombre"]+" "

    #Se ensucia `descripcion`: 12% en None (nulos)

    filas_elegidas=generar_muestra(datos_df,0.12)
    datos_df.loc[filas_elegidas,"descripcion"]=None
    
    #Se ensucia `fecha_inicio`: dos formatos mezclados: "2026-03-02" y "02/03/2026"

    iso=datos_df["fecha_inicio"].dt.strftime("%Y-%m-%d")
    latino=datos_df["fecha_inicio"].dt.strftime("%d/%m/%Y")
    datos_df["fecha_inicio"]=iso
    filas_elegidas=generar_muestra(datos_df,0.30)
    datos_df.loc[filas_elegidas,"fecha_inicio"]=latino.loc[filas_elegidas]

    #Se ensucia `fecha_fin`: 8% en None 

    filas_elegidas=generar_muestra(datos_df,0.08)
    datos_df.loc[filas_elegidas,"fecha_fin"]=None
    
    # 5% ANTERIOR a fecha_inicio (error logico a detectar).

    filas_elegidas=generar_muestra(datos_df,0.05)

    fecha_inicio=pd.to_datetime(
        datos_df["fecha_inicio"],
        format="mixed",
        dayfirst=True
    )

    datos_df.loc[filas_elegidas,"fecha_fin"]=(
        fecha_inicio.loc[filas_elegidas]-pd.Timedelta(days=5)
    )
    #Se ensucia `estado`: variantes: 'en_curso', 'EN CURSO', ' Cerrado '.
    filas_elegidas=generar_muestra(datos_df,0.10)
    datos_df.loc[filas_elegidas,"estado"]=datos_df.loc[filas_elegidas,"estado"].map(escribir_mal)
    
    #5% de las filas repetidas tal cual (duplicados exactos).

    filas_elegidas = generar_muestra(datos_df, 0.05)
    datos_df = pd.concat([datos_df, datos_df.loc[filas_elegidas]], ignore_index=True)








