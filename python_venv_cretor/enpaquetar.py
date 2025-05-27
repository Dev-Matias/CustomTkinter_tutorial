import subprocess

def enpaquetar_para_linux(archivo_python):
    try:
        subprocess.run(['pyinstaller', '--onefile', archivo_python], check=True)
        print(f"El archivo {archivo_python} ha sido empaquetado exitosamente para Linux.")
    except subprocess.CalledProcessError as e:
        print(f"Ocurrió un error al empaquetar el archivo: {e}")

enpaquetar_para_linux('main.py')
