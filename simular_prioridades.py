"""
Define el nivel de atencion del reto. Crea el script `src/simular_prioridades.py`. Con la libreria **Faker** genera 200 filas falsas de la tabla `prioridades`, con las MISMAS columnas que usa Backend II. Despues **ensucia los datos a proposito**: nulos, duplicados, espacios sobrantes, mayusculas mezcladas y formatos distintos. Esos errores son los que vas a arreglar en la etapa de limpieza, asi que tienen que quedar bien puestos.

Usa `Faker("es_CO")` y fija la semilla con `Faker.seed(42)` y `random.seed(42)` para que el resultado sea SIEMPRE el mismo y tu compañero pueda reproducirlo.

OJO: `dias_max_respuesta` NO esta en el modelo de Backend II: es una columna EXTRA solo para este ejercicio de analisis. Dejala anotada como tal en el script.
"""
import random
import uuid
import pandas as pd
from faker import Faker
 
#1. configurar el faker a la region que necesito
fake=Faker("es_CO")

#2. fijar la semilla para que el resultado sea siempre el mismo
Faker.seed(42)
random.seed(42)

#3. identifico los datos que debo simular

# id (texto (UUID))
# nombre (texto)
#  nivel (entero)
#  dias_max_respuesta (entero).

#identificonlos datos o el dato que sea un selector
# 4. identifico los datos o el dato que sea un selector

NIVELES = {"CRITICA": 5, "ALTA": 4, "MEDIA": 3, "BAJA": 2, "MINIMA": 1}
DIAS = {5: 1, 4: 3, 3: 7, 2: 10, 1: 15}

#5 defino mi DATASET
FILAS=200

#6. construyo una funcion para generar los N datos pedidos (LIMPIOS)
def generar_datos_limpios(numeros_datos=FILAS):
    filas=[]
    for _ in range(numeros_datos):
     nombre = random.choice(list(NIVELES.keys()))
     nivel = NIVELES[nombre]
     dias_max_respuesta = DIAS[nivel]

    filas.append({
        
            "id":str(uuid.uuid4()),
            "nombre":random.choice(list(NIVELES.keys())),
            "nivel":NIVELES[nombre],
            "dias_max_respuesta":DIAS[nivel],
        })
       
    return filas 
    
variable_noche=pd.DataFrame(generar_datos_limpios())
        

# Ensuciar los datos 
 
#1, Crear una funcion para definir porcentajes de error 
def generar_muestra(datos,porcentaje):
    return datos.sample(fraccion=porcentaje,random_state=random.randint(0,999)).index

#2. Crear una funcion para escribir mal un texto
def escribir_mal(texto):
    variantes=[texto.lower(),f"{texto.title()}",texto.capitalize()]
    return random.choice(variantes)

#3. Convertir booleanos en texto
def convertir_booleano_texto(valor):
    if valor:
        return random.choice(["SI","1"])
    return random.choice(["NO","0"])

#4. funcion para ensuciar los datos
def ensuciar(datos_df):
    datos_df=datos_df.copy()

#nombre:  variantes: 10% 'ALTA', ' alta ', 'Alta'.
    filas_elegidas=generar_muestra(datos_df,0.10)
    datos_df.loc[filas_elegidas,"nombre"]= datos_df.loc[filas_elegidas,"nombre"].map(escribir_mal)

#Se ensucia `nivel`: a veces como TEXTO ('3'), a veces la palabra ('tres') y 7% en None.
    filas_elegidas=generar_muestra(datos_df,0.05)
    datos_df.loc[filas_elegidas,"nivel"]= datos_df.loc[filas_elegidas,"nivel"].astypec(str)

    filas_elegidas = generar_muestra(datos_df, 0.08)
    datos_df.loc[filas_elegidas, "nivel"] = datos_df.loc[filas_elegidas, "nivel"].map({5: "cinco", 4: "cuatro", 3: "tres", 2: "dos", 1: "uno"})

    filas_elegidas= generar_muestra(datos_df,0.07)
    datos_df.loc[filas_elegidas,"correo"]=None    

#Se ensucia `dias_max_respuesta`: 5% en None y 3% con un valor absurdo (999)
    filas_elegidas=generar_muestra(datos_df,0.05)  
    datos_df-loc[filas_elegidas,"dias_max_respuesta"]=None

    filas_elegidas=generar_muestra(datos_df,0.03)  
    datos_df-loc[filas_elegidas,"dias_max_respuesta"]=999

