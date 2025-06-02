import json
import os

# Cargar preguntas desde un archivo JSON y manejar la interfaz de usuario al salir del programa.
ARCHIVO_JSON = os.path.join(os.path.dirname(__file__), "questions.json")
QUIZ_RESULTS_TXT = os.path.join(os.path.dirname(__file__), "quiz_results.txt")

def load_questions():
    """Carga las preguntas desde un archivo JSON."""
    try:
         with open(ARCHIVO_JSON, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: El archivo '{ARCHIVO_JSON}' no fue encontrado.")
        return []
    except json.JSONDecodeError:
        print(f"Error: El archivo '{ARCHIVO_JSON}' no es un JSON válido.")
        return []
    
def save_results(self):
    with open(QUIZ_RESULTS_TXT, "w") as file:
        file.write(f"Respuestas correctas: {self.respuesta_correcta}\n")
        file.write(f"Respuestas incorrectas: {self.respuesta_incorrecta}\n")

def cargar_respuesta():
    """Carga la respuesta correcta desde el archivo de resultados."""
    try:
        with open(QUIZ_RESULTS_TXT, "r") as file:
            lines = file.readlines()
            if len(lines) >= 2:
                correctas = int(lines[0].strip().split(": ")[1])
                incorrectas = int(lines[1].strip().split(": ")[1])
                return correctas, incorrectas
            else:
                return 0, 0
    except FileNotFoundError:
        return 0, 0
    except ValueError:
        return 0, 0
