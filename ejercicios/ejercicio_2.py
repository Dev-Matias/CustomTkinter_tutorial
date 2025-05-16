import customtkinter as ctk

app = ctk.CTk()
app.geometry("400x300")
app.title("Ejercicio 2") # titulo de la ventana

# Tema de la ventana
ctk.set_appearance_mode("dark") # modo oscuro
ctk.set_default_color_theme("green") # color green

app.mainloop() # bucle principal de la aplicacion