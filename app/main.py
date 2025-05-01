from fastapi import FastAPI
from app.controller.file_controller import router
from fastapi.responses import HTMLResponse
import os

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def root():
    return """
    <h1>API de Procesamiento de TXT</h1>
    <p>Usa la <a href='/docs'>documentación interactiva</a> para probar el sistema.</p>
    """

# Crear carpetas si no existen
os.makedirs("uploads", exist_ok=True)
os.makedirs("output", exist_ok=True)

app.include_router(router, prefix="/archivo", tags=["Procesamiento TXT"])
