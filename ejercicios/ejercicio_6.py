import customtkinter as ctk

app = ctk.CTk()
app.geometry("400x300")
app.title("Ejercicio 6")
# Set the default color theme
ctk.set_appearance_mode("System")  # Modes: "System" (default), "Light", "Dark"
ctk.set_default_color_theme("green")  # Themes: "blue" (default), "green", "dark-blue"

#Widgets basicos CHECKBOX Y SWITCH
checkbox = ctk.CTkCheckBox(app, text="ACEPTO LOS TERMINOS Y CONDICIONES",font=("Arial", 12), text_color="White", fg_color="green", hover_color="grey")
checkbox.pack(pady=20)

#Funcion desabilitar el boton
def desabilitar_btn():
    if switch.get() == 1: # Si el switch está activado
        btn.configure(state="normal")
        btn.configure(fg_color="green", hover_color="green")
        print(switch.get())
    else:
        btn.configure(state="disabled")
        print(switch.get())
#Widget Switch
switch = ctk.CTkSwitch(app, text="ACEPTAR", font=("Arial", 12), text_color="White", state="normal" ,command=desabilitar_btn, fg_color="green")
switch.pack(pady=20)

#Funcion de prueba para el boton
def btn_prueba():
    print("Boton Habilitado")
    print(switch.get())

#Widget Boton
btn = ctk.CTkButton(app, text="ACEPTAR", font=("Arial", 12), text_color="White", fg_color="grey", hover_color="grey", state="disabled",command=btn_prueba)
btn.pack(pady=20) 


app.mainloop()