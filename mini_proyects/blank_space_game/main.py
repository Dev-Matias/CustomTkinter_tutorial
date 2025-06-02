import customtkinter as ctk
from cargar_json import cargar_datos, guardar_puntaje_txt, cargar_puntaje_txt

class RellenarEspaciosApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Rellenar Espacios en Blanco")
        self.geometry("500x400")

        # Load questions from JSON file
        self.preguntas = cargar_datos()

        # Load saved score
        saved_data = cargar_puntaje_txt()
        print(f"Datos guardados: {saved_data}")
        self.puntaje = saved_data.get("puntaje", 0)
        self.correctas = saved_data.get("correctas", 0)
        self.incorrectas = saved_data.get("incorrectas", 0)
        self.pregunta_index = self.correctas + self.incorrectas

        # Create tabs
        self.tabview = ctk.CTkTabview(self, width=450, height=350)
        self.tabview.pack(pady=20)

        self.tab_pregunta = self.tabview.add("Pregunta")
        self.tab_puntaje = self.tabview.add("Puntaje")

        # Create widgets for the Pregunta tab
        self.label_pregunta = ctk.CTkLabel(
            self.tab_pregunta, text="", font=("Arial", 16), wraplength=450
        )
        self.label_pregunta.pack(pady=20)

        self.entry_respuesta = ctk.CTkEntry(self.tab_pregunta, width=200, font=("Arial", 14))
        self.entry_respuesta.pack(pady=10)

        self.boton_verificar = ctk.CTkButton(
            self.tab_pregunta, text="Verificar Respuesta", command=self.verificar_respuesta
        )
        self.boton_verificar.pack(pady=10)

        self.label_resultado = ctk.CTkLabel(
            self.tab_pregunta, text="", font=("Arial", 14), text_color="green"
        )
        self.label_resultado.pack(pady=10)

        self.boton_siguiente = ctk.CTkButton(
            self.tab_pregunta,
            text="Siguiente Pregunta",
            command=self.siguiente_pregunta,
            state="disabled",
        )
        self.boton_siguiente.pack(pady=10)

        # Create widgets for the Puntaje tab
        self.label_puntaje = ctk.CTkLabel(self.tab_puntaje, text=f"Puntaje: {self.puntaje}", font=("Arial", 16))
        self.label_puntaje.pack(pady=20)

        self.label_correctas = ctk.CTkLabel(self.tab_puntaje, text=f"Correctas: {self.correctas}", font=("Arial", 16))
        self.label_correctas.pack(pady=10)

        self.label_incorrectas = ctk.CTkLabel(self.tab_puntaje, text=f"Incorrectas: {self.incorrectas}", font=("Arial", 16))
        self.label_incorrectas.pack(pady=10)

        self.boton_guardar_puntaje = ctk.CTkButton(
            self.tab_puntaje, text="Guardar Puntaje", command=self.guardar_puntaje
        )
        self.boton_guardar_puntaje.pack(pady=10)

        # Mostrar la primera pregunta
        self.mostrar_pregunta()

    def mostrar_pregunta(self):
        if self.pregunta_index < len(self.preguntas):
            pregunta_data = self.preguntas[self.pregunta_index]
            self.label_pregunta.configure(text=pregunta_data["pregunta"])
            self.entry_respuesta.delete(0, ctk.END)  # Limpiar entrada
            self.label_resultado.configure(text="")
            self.boton_verificar.configure(state="normal")
            self.boton_siguiente.configure(state="disabled")
        else:
            self.label_pregunta.configure(text="Fin del quiz!")
            self.label_resultado.configure(
                text=f"Puntaje final: {self.puntaje}/{len(self.preguntas)}"
            )
            self.boton_verificar.configure(state="disabled")
            self.boton_siguiente.configure(state="disabled")

    def verificar_respuesta(self):
        respuesta_usuario = self.entry_respuesta.get().strip()
        pregunta_data = self.preguntas[self.pregunta_index]

        if respuesta_usuario == pregunta_data["respuesta"]:
            self.label_resultado.configure(
                text="¡Respuesta correcta!", text_color="green"
            )
            self.puntaje += 1
            self.correctas += 1
        else:
            self.label_resultado.configure(
                text=f"Respuesta incorrecta. La respuesta era: {pregunta_data['respuesta']}",
                text_color="red",
            )
            self.puntaje -= 1
            self.incorrectas += 1

        self.label_puntaje.configure(text=f"Puntaje: {self.puntaje}")
        self.label_correctas.configure(text=f"Correctas: {self.correctas}")
        self.label_incorrectas.configure(text=f"Incorrectas: {self.incorrectas}")
        self.boton_verificar.configure(state="disabled")
        self.boton_siguiente.configure(state="normal")

    def siguiente_pregunta(self):
        self.pregunta_index += 1
        self.mostrar_pregunta()

    def guardar_puntaje(self):
        guardar_puntaje_txt(self.puntaje, self.correctas, self.incorrectas)
        self.label_resultado.configure(text="Puntaje guardado!", text_color="blue")

if __name__ == "__main__":
    app = RellenarEspaciosApp()
    app.mainloop()