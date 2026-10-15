#Rutina para cobertir una lista de diccionarios en multiples fuentes de informacion
import json
from pathlib import Path

#1. Configuracion (cambiar segun su tabla)
NOMBRE_ENTIDAD="empresa"
CARPETA_PROYECTO=Path(__file__).resolve().parents[2]
#2.1 CREAR LA CARPETA SI NO EXISTE

def preparar_carpeta(carpeta):
    carpeta.mkdir(parents=True, exist_ok=True)    
    return carpeta

#2.2 EXPORTAR A CSV
def exportar_csv(datos_df,carpeta,nombre_archivo):
    ruta=preparar_carpeta(carpeta)/f"{nombre_archivo}.csv"
    datos_df.to_csv(ruta,index=False,sep=";",encoding="utf-8-sig")
    return ruta

#2.3 EXPORTAR A JSON
def exportar_json(data_df,carpeta,nombre_archivo):
    ruta=preparar_carpeta(carpeta)/f"{nombre_archivo}.json"
    data_df.to_json(ruta,orient="records",date_format="iso",ident=2)
    return ruta

#2.4 EXPORTAR A EXCEL
def exportar_excel(datos_df,carpeta,nombre_archivo):
    ruta=preparar_carpeta(carpeta)/f"{nombre_archivo}.xlsx"
    datos_df.to_excel(ruta,index=false,engine="openpyxl")
    return ruta 

#3. GENERO LOS ARCHIVOS EN MI PROYECTO

def exportar_usuarios_crudos(datos_sucios_df):
    return[
        exportar_csv(datos_sucios_df,CARPETA_CRUDOS,f"{NOMBRE_ENTIDAD}_crudo"),

        exportar_json(datos_sucios_df,CARPETA_CRUDOS,f"{NOMBRE_ENTIDAD}_"),

        exportar_excel(datos_sucios_df,CARPETA_CRUDOS,f"{NOMBRE_ENTIDAD}_")
    ]