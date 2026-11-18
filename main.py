import random
from datetime import datetime
from typing import Dict, List
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(
    title="API Simulador SMS Chile",
    description="API para generar números móviles chilenos (+56 9) y simular recepción de SMS.",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

bandejas_sms: Dict[str, List[dict]] = {}

class MensajeEntrante(BaseModel):
    remitente: str
    texto: str

@app.get("/")
def inicio():
    return {
        "estado": "en_linea",
        "mensaje": "API Simulador SMS Chile funcionando. Visita /docs para probar los endpoints."
    }

@app.post("/numeros/generar")
def generar_numero_chileno():
    numero_aleatorio = random.randint(10000000, 99999999)
    numero_completo = f"+569{numero_aleatorio}"
    
    bandejas_sms[numero_completo] = []
    return {
        "numero": numero_completo,
        "formato_visual": f"+56 9 {str(numero_aleatorio)[:4]} {str(numero_aleatorio)[4:]}",
        "estado": "activo"
    }

@app.post("/numeros/{numero}/simular-sms")
def recibir_sms_simulado(numero: str, mensaje: MensajeEntrante):
    if numero not in bandejas_sms:
        raise HTTPException(status_code=404, detail="Número no encontrado. Debes generarlo primero.")
    
    nuevo_sms = {
        "de": mensaje.remitente,
        "mensaje": mensaje.texto,
        "fecha_hora": datetime.now().isoformat()
    }
    bandejas_sms[numero].append(nuevo_sms)
    return {"status": "SMS recibido", "datos": nuevo_sms}

@app.get("/numeros/{numero}/mensajes")
def leer_mensajes(numero: str):
    if numero not in bandejas_sms:
        raise HTTPException(status_code=404, detail="Número no encontrado.")
    
    return {
        "numero": numero,
        "total_mensajes": len(bandejas_sms[numero]),
        "mensajes": bandejas_sms[numero]
    }
