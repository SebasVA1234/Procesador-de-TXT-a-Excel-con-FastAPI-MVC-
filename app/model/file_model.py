from pydantic import BaseModel

class ProcesamientoConfig(BaseModel):
    lineas_por_fila: int