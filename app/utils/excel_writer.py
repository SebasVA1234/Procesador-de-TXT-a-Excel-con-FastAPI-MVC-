import pandas as pd
import os

def procesar_txt_y_guardar_excel(ruta_txt, lineas_por_fila, columnas, nombre_excel):
    with open(ruta_txt, 'r', encoding='utf-8') as archivo:
        lineas = [linea.strip() for linea in archivo if linea.strip() != ""]

    if len(lineas) % lineas_por_fila != 0:
        raise ValueError("Las líneas del archivo no son múltiplo del grupo definido.")

    filas = [lineas[i:i + lineas_por_fila] for i in range(0, len(lineas), lineas_por_fila)]

    df = pd.DataFrame(filas, columns=columnas)

    ruta_output = os.path.join("output", nombre_excel)
    df.to_excel(ruta_output, index=False)

    return ruta_output
