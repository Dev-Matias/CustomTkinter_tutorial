import customtkinter as ctk

app = ctk.CTk()
app.geometry("400x300")
app.title("Ejercicio 3") # titulo de la ventana

# Tema de la ventana
ctk.set_appearance_mode("dark") # modo oscuro
ctk.set_default_color_theme("dark-blue") # color principal dark-blue

# Widgets Basicos 
label = ctk.CTkLabel(app, text="Ejercicio 3",font=("Arial",24),bg_color="red") # etiqueta con fuente Arial de tamaño 24 y color rojo
label.pack(pady=10) # añade un margen de 10 pixeles en el eje y

app.mainloop() # bucle principal de la aplicacion