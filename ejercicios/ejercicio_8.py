import customtkinter as ctk


app = ctk.CTk()
app.geometry("600x400")
app.title("Ejercicio 8")
# Set the default color theme
ctk.set_appearance_mode("System")  # Modes: "System" (default), "Light", "Dark"
ctk.set_default_color_theme("blue")  # Themes: "blue" (default), "green", "dark-blue"
# FUNCION DE PRUEBA PARA EL COMBOBOX
def combo_box_prueba(value):
    print(combo_box.get())# optener el valor seleccionado

    print("Opcion seleccionada:", value)# optener el valor seleccionado pasado por el evento
 
# Widget Avanzado ComboBox
combo_box = ctk.CTkComboBox(app, values=["Opcion 1", "Opcion 2", "Opcion 3"], font=("Arial", 12), text_color="White", fg_color="green",command=combo_box_prueba)
combo_box.pack(pady=20)

#Slider actualizar valor de la etiqueta
def actualizar_valor_slider(value):
    label.configure(text=f"Valor del Slider: {value}")

# Widget Avanzado Slider
slider = ctk.CTkSlider(app, from_=0, to=100, number_of_steps=10, command=actualizar_valor_slider)
slider.pack(pady=20)
label = ctk.CTkLabel(app, text="Valor del Slider: 0")
label.pack(pady=20)
app.mainloop()
