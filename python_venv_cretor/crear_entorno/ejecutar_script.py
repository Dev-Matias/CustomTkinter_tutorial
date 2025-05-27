import subprocess
import os

def ejecutar_script_sh(nombre_script):
    """
    Ejecuta un script .sh ubicado en el mismo directorio.

    Args:
        nombre_script (str): El nombre del archivo del script .sh.
    """
    try:
        # Asegurarse de que el script tenga permisos de ejecución
        os.chmod(nombre_script, 0o755)  # rwxr-xr-x

        # Construir el comando a ejecutar
        comando = ['./' + nombre_script]

        # Ejecutar el comando
        proceso = subprocess.Popen(comando, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = proceso.communicate()

        # Decodificar la salida a texto
        stdout_str = stdout.decode('utf-8')
        stderr_str = stderr.decode('utf-8')

        # Imprimir la salida y los errores (si los hay)
        print("Salida del script:")
        print(stdout_str)

        if stderr_str:
            print("\nErrores del script:")
            print(stderr_str)

        # Devolver el código de salida del proceso
        return proceso.returncode

    except FileNotFoundError:
        print(f"Error: El script '{nombre_script}' no se encontró en el directorio actual.")
        return 1
    except Exception as e:
        print(f"Ocurrió un error al ejecutar el script: {e}")
        return 1
