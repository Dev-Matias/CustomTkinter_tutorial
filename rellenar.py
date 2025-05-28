import json
import os

ARCHIVO_JSON = "preguntas_respuestas.json"


def cargar_datos():
    if os.path.exists(ARCHIVO_JSON):
        with open(ARCHIVO_JSON, "r") as archivo:
            return json.load(archivo)
    return []


def guardar_datos(datos):
    with open(ARCHIVO_JSON, "w") as archivo:
        json.dump(datos, archivo, indent=4)


def agregar_entrada():
    pregunta = input("\nIngresa tu pregunta: ")
    respuesta = input("Ingresa la respuesta: ")
    return {"pregunta": pregunta, "respuesta": respuesta}


def mostrar_entradas(datos):
    print("\n--- Listado de Preguntas y Respuestas ---")
    for idx, entrada in enumerate(datos, 1):
        print(f"\nEntrada {idx}:")
        print(f"Pregunta: {entrada['pregunta']}")
        print(f"Respuesta: {entrada['respuesta']}")
    print("\n----------------------------------------")


def menu():
    datos = cargar_datos()

    while True:
        print("\nMenú:")
        print("1. Agregar nueva pregunta-respuesta")
        print("2. Consultar listado")
        print("3. Salir")

        opcion = input("Selecciona una opción (1-3): ")

        if opcion == "1":
            nueva_entrada = agregar_entrada()
            datos.append(nueva_entrada)
            guardar_datos(datos)
            print("\n¡Entrada guardada exitosamente!")

        elif opcion == "2":
            if datos:
                mostrar_entradas(datos)
            else:
                print("\nNo hay entradas para mostrar.")

        elif opcion == "3":
            print("\n¡Hasta luego!")
            break

        else:
            print("\nOpción no válida. Por favor ingresa 1, 2 o 3.")


if __name__ == "__main__":
    menu()
