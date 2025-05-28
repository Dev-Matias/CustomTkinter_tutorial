import customtkinter as ctk

app = ctk.CTk()
app.geometry("600x400")
app.title("Ejercicio 7")
# Set the default color theme
ctk.set_appearance_mode("System")  # Modes: "System" (default), "Light", "Dark"
ctk.set_default_color_theme("blue")  # Themes: "blue" (default), "green", "dark-blue"

# Widget Sistema de grillas manual
label1 = ctk.CTkLabel(app, text="Sistema de grillas")
label1.grid(row=0, column=0, padx=20, pady=20)
label2 = ctk.CTkLabel(app, text="Sistema de grillas")
label2.grid(row=0, column=1, padx=20, pady=20)
label3 = ctk.CTkLabel(app, text="Sistema de grillas")
label3.grid(row=0, column=2, padx=20, pady=20)

btn = ctk.CTkButton(app, text="Boton 1")
btn.grid(row=1, column=0, padx=20, pady=20)
btn2 = ctk.CTkButton(app, text="Boton 2")
btn2.grid(row=1, column=1, padx=20, pady=20)
btn3 = ctk.CTkButton(app, text="Boton 3")
btn3.grid(row=1, column=2, padx=20, pady=20)
# Widget grid creadas dinamicamente grid 3x3
for i in range(3):
    for j in range(3):
        label = ctk.CTkLabel(app, text=f"Label {i},{j}")
        label.grid(row=i+2, column=j, padx=20, pady=20)



app.mainloop()