'''
Organizacion que registra o propone retos. Crea el script `src/simular_empresas.py`. 
Con la libreria **Faker** genera 300 filas falsas de la tabla `empresas`, con las MISMAS columnas que usa Backend II. 
Despues **ensucia los datos a proposito**: nulos, duplicados, espacios sobrantes, mayusculas mezcladas y formatos distintos. 
Esos errores son los que vas a arreglar en la etapa de limpieza, asi que tienen que quedar bien puestos.

Usa `Faker("es_CO")` y fija la semilla con `Faker.seed(42)` y `random.seed(42)` para que el resultado sea SIEMPRE el mismo y tu compañero pueda reproducirlo.

'''
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
#id (texto (UUID))
# nombre (texto)
# nit (texto)
# sector (texto) seleccionable por el usuario
# contacto (texto)
# correo (texto)
# telefono (texto)
# activa (booleano)

#4. identifico los datos o el dato que sea un selector
SECTORES=["TECNOLOGIAS","SALUD","ALIMENTOS"]

#5 defino mi DATASET
FILAS=300

#6. construyo una funcion para generar los N datos pedidos (LIMPIOS)
def generar_datos_limpios(numeros_datos=FILAS):
    filas=[]
    for _ in range(numeros_datos):

        filas.append({
            "id":str(uuid.uuid4()),
            "nombre":fake.company(),
            "nit":fake.numerify("##########"),
            "sector":random.choice(SECTORES),
            "contacto":fake.name(),
            "correo":fake.company_email(),
            "telefono":fake.numerify("+57 ### ### ####"),
            "activa":random.choice([True, False])
        })
    return filas
variable_noche=pd.DataFrame(generar_datos_limpios())

#Ensuciar los datos

#1. crear una funcion para definir porcentaje de error
def generar_muestra(datos,porcentaje):
    return datos.sample(fraccion=porcentaje,
    random_state=random.randint(0, 9999)).index

#2. crear una funcion para escribir mal un texto
def escribir_mal(texto):
    variantes=[texto.lower(),f" {texto.title()} ", texto.capitalize(),]
    return random.choice(variantes)

#3. crear una funcion para convertir booleanos a texto
def convertir_booleano_texto(valor):
    if valor:
        return random.choice(["SI","1",])
    return random.choice(["NO","0",])

#4. Funcion para ensuciar los datos
def ensuciar(datos_df):
    datos_df=datos_df.copy()

    #nombre: 10% con espacios sobrantes, el 15% con mayusculas
    filas_elegidas=generar_muestra(datos_df, 0.10)
    datos_df.loc[filas_elegidas, "nombre"]=" "+datos_df.loc[filas_elegidas, "nombre"]+" "

    filas_elegidas=generar_muestra(datos_df, 0.15)
    datos_df.loc[filas_elegidas, "nombre"]=datos_df.loc[filas_elegidas, "nombre"].str.upper()

    #nit: la mitad con puntos y guiones (900.123.456-7) y la otra mitad sin nada (9001234567).
    filas_elegidas=generar_muestra(datos_df,0.5)
    datos_df.loc[filas_elegidas, "nit"]=datos_df.loc[filas_elegidas, "nit"].str.replace(",",".")

    filas_elegidas=generar_muestra(datos_df,0.5)
    datos_df.loc[filas_elegidas, "nit"]=datos_df.loc[filas_elegidas, "nit"].str.replace("-","")

    #sector: variantes del mismo sector: 'Logistica', 'LOGISTICA', ' logistica 
    filas_elegidas=generar_muestra(datos_df,0.08)
    datos_df.loc[filas_elegidas, "sector"]=datos_df.loc[filas_elegidas,"sector"].map(escribir_mal)

    #contacto: 8% en None (nulos).
    filas_elegidas=generar_muestra(datos_df, 0.08)
    datos_df.loc[filas_elegidas, "contacto"]=None

    #correo: 6% sin la arroba (correo invalido).
    filas_elegidas=generar_muestra(datos_df, 0.06)
    datos_df.loc[filas_elegidas, "correo"]=datos_df.loc[filas_elegidas, "correo"].str.replace("@","", regex=False)

    #telefono: tres formatos mezclados: '3001234567', '300 123 4567', '+57 300-123-4567'.
    filas_elegidas=generar_muestra(datos_df, 0.33)
    datos_df.loc[filas_elegidas, "telefono"]=datos_df.loc[filas_elegidas, "telefono"].str.replace(" ","")
        
    #activa: a veces como texto: 'SI', 'No', '1', '0'.
    filas_elegidas=generar_muestra(datos_df, 0.3)
    datos_df.loc[filas_elegidas,"activo"]=datos_df.loc[filas_elegidas, "activo"].map(convertir_booleano_texto)

    #5% de las filas repetidas tal cual (duplicados exactos).
    filas_elegidas=generar_muestra(datos_df, 0.05)
    datos_df=pd.concat([datos_df, datos_df.loc[filas_elegidas]], ignore_index=True)

    #3% de los `nit` repetidos entre empresas distintas (el NIT deberia ser unico).
    filas_elegidas=generar_muestra(datos_df, 0.03)
    datos_df.loc[filas_elegidas, "nit"]=datos_df.loc[filas_elegidas, "nit"].sample(frac=1, random_state=random.randint(0, 9999)).values






    
