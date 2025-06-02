import json
import os
from datetime import datetime

ARCHIVO_JSON = os.path.join(os.path.dirname(__file__), "questions.json")
PUNTAJE_TXT = os.path.join(os.path.dirname(__file__), "puntaje.txt")
def cargar_datos():
    if os.path.exists(ARCHIVO_JSON):
        with open(ARCHIVO_JSON, "r") as archivo:
            return json.load(archivo)
    return []

def guardar_puntaje_txt(puntaje, correctas, incorrectas):
    data = {
        "puntaje": puntaje,
        "correctas": correctas,
        "incorrectas": incorrectas,
        "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    with open(PUNTAJE_TXT, "w") as archivo:
        json.dump(data, archivo, indent=4)

def cargar_puntaje_txt():
    if os.path.exists(PUNTAJE_TXT):
        with open(PUNTAJE_TXT, "r") as archivo:
            return json.load(archivo)
    return {"puntaje": 0, "correctas": 0, "incorrectas": 0, "fecha": ""}