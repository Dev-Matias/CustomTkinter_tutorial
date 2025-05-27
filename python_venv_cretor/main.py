import customtkinter as ctk
import tkinter as tk  # Importa tkinter para las constantes de posición
import os
import subprocess
def btn_crear_carpeta():
    """
    Función para crear una carpeta en el home 
    con el nombre provisto por el usuario
    """
    texto_ingresado = entrada.get()
    home_dir = os.path.expanduser("~")
    # crear la carpeta
    nueva_carpeta_path = os.path.join(home_dir,texto_ingresado)
    try:
        # Crear la carpeta
        os.makedirs(nueva_carpeta_path, exist_ok=True)
        print(f"Carpeta '{texto_ingresado}' creada exitosamente en {nueva_carpeta_path}.")
       
        # Cambiar al directorio de la carpeta creada
        os.chdir(nueva_carpeta_path)
        print(f"Posicionado en la carpeta '{nueva_carpeta_path}'.")

   # Ejecutar el comando para crear el entorno virtual
        subprocess.run(["python3", "-m", "venv", ".venv"], check=True)
        print("Entorno virtual creado exitosamente.")
    # Activar el ebntorno Virtual
       
    except Exception as e:
        print(f"Error al crear la carpeta: {e}")
    etiqueta_resultado.configure(text=f"carpeta creada en: {nueva_carpeta_path} y entorno virtual creado")
    entrada.delete(0, ctk.END)

def boton_instalar_click():
    """
    Función que se ejecuta al hacer clic en el botón "Instalar".
    Muestra un mensaje de instalación simulada en la consola.
    """
   
    print("Instalando módulos seleccionados...")
    for nombre_modulo, var_check in checkboxes_data:
        if var_check.get():
            print(f"  Instalando: {nombre_modulo}")
            subprocess.run([f"pip3 install {nombre_modulo}"],check=True)
    print("Instalación completada .")

    # Opcional: Mostrar mensaje en la GUI
    etiqueta_resultado.configure(text="Instalación simulada completada. Ver consola.")

def boton_actualizar_click():
    """
    Instalar los modulos seleccionados
    """
    print("Actualizando módulos...")
    # Aquí iría la lógica para actualizar los módulos
    print("Actualización completada (simulada).")

    # Opcional: Mostrar mensaje en la GUI
    etiqueta_resultado.configure(text="Actualización simulada completada. Ver consola.")

# Crear la ventana principal
ventana = ctk.CTk()
ventana.title("Mi App de Instalación de Módulos")
ventana.geometry("400x500")  # Tamaño de la ventana
# Deshabilitar la capacidad de cambiar el tamaño de la ventana
ventana.resizable(False, False)  # El primer False deshabilita el cambio de ancho, el segundo el de alto
ctk.set_appearance_mode("system")
ctk.set_default_color_theme("dark-blue")
frame1 = ctk.CTkFrame(ventana,width=600,height=200,corner_radius=10)
frame1.pack(padx=10,pady=10)
frame2 = ctk.CTkFrame(ventana,width=100,height=100,corner_radius=10)
frame2.pack(padx=10,pady=10)
frame3 = ctk.CTkFrame(ventana,width=600,height=200,corner_radius=10)
frame3.pack(padx=10,pady=10)
# Crear la entrada de texto y el botón "Aceptar"
entrada = ctk.CTkEntry(frame1, width=200)
entrada.pack(side=ctk.LEFT, padx=10, pady=20)
boton_aceptar = ctk.CTkButton(frame1, text="Crear Carpeta", command=btn_crear_carpeta)
boton_aceptar.pack(side=ctk.LEFT, padx=10, pady=20)

# Crear la etiqueta "Módulos útiles" y el botón "Instalar"
etiqueta_modulos = ctk.CTkLabel(frame2, text="Módulos útiles:",width=200)
etiqueta_modulos.pack(side=ctk.LEFT, padx=10, pady=10)  # Alineado a la izquierda
boton_instalar = ctk.CTkButton(frame2, text="Instalar", command=boton_instalar_click)
boton_instalar.pack(side=ctk.LEFT, padx=10, pady=10 )  # Alineado a la izquierda
boton_actualizar = ctk.CTkButton(frame2, text="Actualizar", command=boton_actualizar_click)
boton_actualizar.pack(side=ctk.LEFT, padx=10, pady=10)

# Crear la grilla de etiquetas y checkboxes
frame_grilla = ctk.CTkFrame(frame3)  # Un frame para contener la grilla
frame_grilla.pack(padx=10, pady=20)

# Datos de los módulos y variables de control para los checkboxes
checkboxes_data = [
    ("requests", ctk.BooleanVar()),
    ("beautifulsoup4", ctk.BooleanVar()),
    ("selenium", ctk.BooleanVar()),
    ("pillow", ctk.BooleanVar()),
    ("numpy", ctk.BooleanVar()),
    ("pandas", ctk.BooleanVar()),
    ("matplotlib", ctk.BooleanVar()),
    ("scikit-learn", ctk.BooleanVar()),
    ("flask", ctk.BooleanVar()),
    ("django", ctk.BooleanVar()),
]

# Crear las etiquetas y checkboxes en la grilla
for i, (nombre_modulo, var_check) in enumerate(checkboxes_data):
    etiqueta_modulo = ctk.CTkLabel(frame_grilla, text=nombre_modulo)
    checkbox_modulo = ctk.CTkCheckBox(frame_grilla, text="", variable=var_check)  # Checkbox sin texto

    # Colocar en la grilla
    etiqueta_modulo.grid(row=i // 2, column=(i % 2) * 2, padx=5, pady=5, sticky=tk.W)  # Alineado a la izquierda
    checkbox_modulo.grid(row=i // 2, column=(i % 2) * 2 + 1, padx=5, pady=5, sticky=tk.W)

# Crear una etiqueta para mostrar el resultado de la acción
etiqueta_resultado = ctk.CTkLabel(frame3, text="Se crea `.venv` para manejar los modulos fuera del sistema", wraplength=350)
etiqueta_resultado.pack(side=ctk.BOTTOM, padx=10, pady=20)

# Iniciar el bucle principal de la aplicación
ventana.mainloop()
