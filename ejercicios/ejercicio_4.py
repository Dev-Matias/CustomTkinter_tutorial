import customtkinter as ctk

def button_function():
    print("Boton Precionado") # imprime en la consola el texto Botton Precisonado
    label.configure(text="Ejercicio 4") # cambia el texto de la etiqueta a Botton Precionado


app = ctk.CTk()
app.geometry("400x300")
app.title("Ejercicio 4") 
# Tema de la ventana
ctk.set_appearance_mode("dark") # modo oscuro
ctk.set_default_color_theme("green") # color green

# Widgets Basicos
label = ctk.CTkLabel(app, text="Texto a Cambiar",font=("Arial",24),fg_color="blue") # etiqueta con fuente Arial de tamaño 24 y color rojo
label.pack(pady=10) # añade un margen de 10 pixeles en el eje y

# Boton
button = ctk.CTkButton(app, text="Precinar", command=button_function) # boton con texto Ejercicio 4
button.pack(pady=10) # añade un margen de 10 pixeles en el eje y

app.mainloop() # bucle principal de la aplicacion