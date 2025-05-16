import customtkinter as tk

app = tk.CTk()
app.geometry("400x300")
app.title("Ejercicio 5")

# Set the default color theme
app.set_appearance_mode("System")  
app.set_default_color_theme("blue")  # Themes: "blue" (default), "green", "dark-blue"

#Widget Entrada de texto
entry = tk.CTkEntry(app, placeholder_text="Escribe algo aquí")
entry.pack(pady=20)
# Widget Botón
def on_button_click():
    user_input = entry.get()
    print(f"Texto ingresado: {user_input}")
button = tk.CTkButton(app, text="Enviar", command=on_button_click)
button.pack(pady=20)


app.mainloop()