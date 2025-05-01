from app.utils.excel_writer import procesar_txt_y_guardar_excel

def procesar_archivo_service(nombre_archivo: str, lineas_por_fila: int):
    ruta_txt = f"uploads/{nombre_archivo}"
    columnas = ["Nro.", "Florícola", "Monto a pagar", "Periodo", "Detalle"]
    nombre_excel = nombre_archivo.replace(".txt", ".xlsx")
    return procesar_txt_y_guardar_excel(ruta_txt, lineas_por_fila, columnas, nombre_excel)
