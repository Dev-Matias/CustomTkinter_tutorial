import customtkinter as ctk

# Configuración inicial de CustomTkinter
ctk.set_appearance_mode("System")  # Modo oscuro/claro
ctk.set_default_color_theme("blue")  # Tema azul

# Lista de preguntas con espacios en blanco
preguntas = [
    {
        "texto": "La función ___() se usa para imprimir en la consola en Python.",
        "respuesta_correcta": "print",
    },
    {
        "texto": "En Python, el operador ___ se utiliza para comparar igualdad.",
        "respuesta_correcta": "==",
    },
    {
        "texto": "El tipo de dato ___ se usa para almacenar números enteros.",
        "respuesta_correcta": "int",
    },
]


class RellenarEspaciosApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Rellenar Espacios en Blanco")
        self.geometry("500x400")

        self.pregunta_index = 0
        self.puntaje = 0

        # Crear widgets
        self.label_pregunta = ctk.CTkLabel(
            self, text="", font=("Arial", 16), wraplength=450
        )
        self.label_pregunta.pack(pady=20)

        self.entry_respuesta = ctk.CTkEntry(self, width=200, font=("Arial", 14))
        self.entry_respuesta.pack(pady=10)

        self.boton_verificar = ctk.CTkButton(
            self, text="Verificar Respuesta", command=self.verificar_respuesta
        )
        self.boton_verificar.pack(pady=10)

        self.label_resultado = ctk.CTkLabel(
            self, text="", font=("Arial", 14), text_color="green"
        )
        self.label_resultado.pack(pady=10)

        self.boton_siguiente = ctk.CTkButton(
            self,
            text="Siguiente Pregunta",
            command=self.siguiente_pregunta,
            state="disabled",
        )
        self.boton_siguiente.pack(pady=10)

        self.label_puntaje = ctk.CTkLabel(self, text="Puntaje: 0", font=("Arial", 16))
        self.label_puntaje.pack(pady=10)

        # Mostrar la primera pregunta
        self.mostrar_pregunta()

    def mostrar_pregunta(self):
        if self.pregunta_index < len(preguntas):
            pregunta_data = preguntas[self.pregunta_index]
            self.label_pregunta.configure(text=pregunta_data["texto"])
            self.entry_respuesta.delete(0, ctk.END)  # Limpiar entrada
            self.label_resultado.configure(text="")
            self.boton_verificar.configure(state="normal")
            self.boton_siguiente.configure(state="disabled")
        else:
            self.label_pregunta.configure(text="Fin del quiz!")
            self.label_resultado.configure(
                text=f"Puntaje final: {self.puntaje}/{len(preguntas)}"
            )
            self.boton_verificar.configure(state="disabled")
            self.boton_siguiente.configure(state="disabled")

    def verificar_respuesta(self):
        respuesta_usuario = self.entry_respuesta.get().strip()
        pregunta_data = preguntas[self.pregunta_index]

        if respuesta_usuario == pregunta_data["respuesta_correcta"]:
            self.label_resultado.configure(
                text="¡Respuesta correcta!", text_color="green"
            )
            self.puntaje += 1
        else:
            self.label_resultado.configure(
                text=f"Respuesta incorrecta. La respuesta era: {pregunta_data['respuesta_correcta']}",
                text_color="red",
            )

        self.label_puntaje.configure(text=f"Puntaje: {self.puntaje}")
        self.boton_verificar.configure(state="disabled")
        self.boton_siguiente.configure(state="normal")

    def siguiente_pregunta(self):
        self.pregunta_index += 1
        self.mostrar_pregunta()


if __name__ == "__main__":
    app = RellenarEspaciosApp()
    app.mainloop()
