import customtkinter as ctk

app = ctk.CTk()
app.geometry("400x300")
app.title("Ejercicio 5")

# Set the default color theme
ctk.set_appearance_mode("System")  # Modes: "System" (default), "Light", "Dark"
ctk.set_default_color_theme("blue")  # Themes: "blue" (default), "green", "dark-blue"

#Widget Etiqueta
label = ctk.CTkLabel(app, text="")
label.pack(pady=20)

#Widget Entrada de texto
entry = ctk.CTkEntry(app, placeholder_text="Escribe algo aquí")
entry.pack(pady=20)

# optener el texto ingresado
def optener_texto():
    user_input = entry.get()
    entry.delete(0, ctk.END)  # Limpiar el campo de entrada
    label.configure(text=f"Texto Ingresado: {user_input}")
    print(f"Texto ingresado: {user_input}")


# Botón para enviar el texto
btn = ctk.CTkButton(app, text="Enviar", command=optener_texto)
btn.pack(pady=20)


app.mainloop()