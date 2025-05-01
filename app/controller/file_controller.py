from fastapi import APIRouter, UploadFile, File, Form
from fastapi.responses import FileResponse
import shutil
import os
from app.services.file_service import procesar_archivo_service

router = APIRouter()

@router.post("/procesar/")
async def procesar_archivo(
    file: UploadFile = File(...),
    lineas_por_fila: int = Form(...)
):
    ruta_destino = f"uploads/{file.filename}"
    with open(ruta_destino, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    ruta_excel = procesar_archivo_service(file.filename, lineas_por_fila)
    return FileResponse(ruta_excel, filename=os.path.basename(ruta_excel))
