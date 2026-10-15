#rutina para convertir una lista de disccionario en multiples fuentes de informacion
import json
from pathlib import Path

#1. Configuracion (cambiar segun su tabla)
NOMBRE_ENTIEDAD="reto"
CARPETA_PROYECTO=Path(__file__).resolve().parent[2]
CARPETA_CRUDOS=CARPETA_PROYECTO/"datos"/"crudos"
CARPETA_LIMPIOS=CARPETA_PROYECTO/"datos"/"limpios"
CARPETA_REPORTES=CARPETA_PROYECTO/"datos"/"reportes"

#2. Funciones genericas para elaborar los archivos
#2.1. CREAR LA CARPETA SI NO EXISTE
def preparar_carpeta(carpeta):
    carpeta.mkdir(parents=True, exit_ok=True)
    return carpeta
#2.2. EXPORTAR A CSV
def exporta_csv(datos_df,carpeta,nombre_archivo):
    ruta=preparar_carpeta(carpeta)/f"{nombre_archivo}.csv"
    datos_df.to_csv(ruta,index=False,sep=";",encoding="utf-8-sig")
    return ruta

#2.3. EXPORTAR A JSON 
def exportar_json(datos_df,carpeta,nombre_archivo):
    ruta=preparar_carpeta(carpeta)/f"{nombre_archivo}.json"
    datos_df.to_json(ruta,orient="records",date_format="iso",ident=2)
    return ruta

#2.4. EXPORTAR A EXCEL 
def exportar_excel(datos_df,carpeta,nombre_archivo):
    ruta=preparar_carpeta(carpeta)/f"{nombre_archivo}.xlsx"
    datos_df.to_excel(ruta,index=False,engine="openpyxl")
    return ruta

#3 GENERO LOS ARCHIVOS EN MI PROYECTO
def exportar_usuarios_crudos(datos_sucios_df):
    return[
        exportar_csv(datos_sucios_df,CARPETA_CRUDOS,f"{NOMBRE_ENTIDAD}_crudo"),

        exportar_json(datos_sucios_df,CARPETA_CRUDOS,f"{NOMBRE_ENTIDAD}_"),

        exportar_excel(datos_sucios_df,CARPETA_CRUDOS,f"{NOMBRE_ENTIDAD}_")
    ]