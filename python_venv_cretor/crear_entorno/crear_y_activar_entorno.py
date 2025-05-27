import subprocess
import sys
import os
from ejecutar_script import ejecutar_script_sh

def crear_y_activar_venv(nombre_entorno="venv", instalar_paquetes=True):
    """
    Crea un entorno virtual de Python, lo activa e instala paquetes (opcional).

    Args:
        nombre_entorno (str): El nombre que se le dará al entorno virtual.
            Por defecto es "mi_entorno".
        instalar_paquetes (bool): Indica si se deben instalar paquetes (ej., requests).
            Por defecto es True.
    """
    try:
        # 1. Determinar el comando para crear el entorno virtual
        if sys.platform.startswith("win"):
            crear_venv_comando = ["python", "-m", "venv", nombre_entorno]
        else:
            crear_venv_comando = ["python3", "-m", "venv", nombre_entorno]

        # 2. Crear el entorno virtual
        print(f"Creando entorno virtual en ./{nombre_entorno}...")
        resultado_creacion = subprocess.run(
            crear_venv_comando,
            check=True,  # Lanza una excepción si el comando falla
            capture_output=True,
            text=True,
        )
        print(resultado_creacion.stdout)
        print("Entorno virtual creado exitosamente.")

        # 3. Activar el entorno virtual
        print("Activando el entorno virtual...")
        if sys.platform.startswith("win"):
            activar_script = os.path.join(nombre_entorno, "Scripts", "activate.bat")
            activar_comando = [activar_script]
        else:
            ejecutar_script_sh("activar_entorno.sh")
        # En Windows, activamos el entorno en el mismo proceso de Python
        if sys.platform.startswith("win"):
            subprocess.run(activar_comando, shell=True, check=True)
            print("Entorno virtual activado. Ahora puedes usar 'pip' directamente.")
        else:
            # En sistemas tipo Unix, esto es más complicado y generalmente se hace en un nuevo shell.
            print(
                "Entorno virtual activado. Debes ejecutar 'source mi_entorno/bin/activate' en tu terminal."
            )
            print("Luego podrás usar 'pip3'.")

        # 4. Instalar paquetes (opcional)
        if instalar_paquetes:
            print("Instalando paquetes...")
            if sys.platform.startswith("win"):
                pip_comando = [
                    os.path.join(nombre_entorno, "Scripts", "pip"),
                    "install",
                    "requests",
                ]
            else:
                pip_comando = [
                    os.path.join(nombre_entorno, "bin", "pip3"),
                    "install",
                    "requests",
                ]

            resultado_instalacion = subprocess.run(
                pip_comando,
                check=True,
                capture_output=True,
                text=True,
            )
            print(resultado_instalacion.stdout)
            print("Paquetes instalados exitosamente.")
        else:
            print("No se instalarán paquetes.")

    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        print(f"Salida del error:\n{e.stderr}")
        sys.exit(1)
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
        sys.exit(1)


if __name__ == "__main__":
    # Llama a la función para crear y activar el entorno virtual
    # Puedes cambiar el nombre del entorno si lo deseas
    crear_y_activar_venv()
