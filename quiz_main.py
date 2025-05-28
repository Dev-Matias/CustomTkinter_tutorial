import json
import customtkinter as ctk


class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz App")
        self.root.geometry("600x400")

        # Cargar preguntas desde el archivo JSON
        self.questions = self.load_questions("questions.json")
        self.current_question_index = 0
        self.score = 0

        # Crear la interfaz
        self.create_widgets()

    def load_questions(self, file_path):
        """Carga las preguntas desde un archivo JSON."""
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"Error: El archivo '{file_path}' no fue encontrado.")
            return []
        except json.JSONDecodeError:
            print(f"Error: El archivo '{file_path}' no es un JSON válido.")
            return []

    def create_widgets(self):
        """Crea los widgets de la interfaz."""
        # Título
        self.title_label = ctk.CTkLabel(
            self.root, text="Bienvenido al Quiz!", font=("Arial", 24, "bold")
        )
        self.title_label.pack(pady=20)

        # Pregunta
        self.question_label = ctk.CTkLabel(
            self.root, text="", font=("Arial", 18), wraplength=500
        )
        self.question_label.pack(pady=10)

        # Botones de respuesta
        self.answer_buttons = []
        for i in range(4):  # Suponemos 4 opciones por pregunta
            button = ctk.CTkButton(
                self.root, text="", command=lambda i=i: self.check_answer(i)
            )
            button.pack(pady=5, fill="x", padx=20)
            self.answer_buttons.append(button)

        # Botón Siguiente
        self.next_button = ctk.CTkButton(
            self.root, text="Siguiente", command=self.next_question, state="disabled"
        )
        self.next_button.pack(pady=20)

        # Mostrar la primera pregunta
        self.show_question()

    def show_question(self):
        """Muestra la pregunta actual."""
        if self.current_question_index < len(self.questions):
            question_data = self.questions[self.current_question_index]
            self.question_label.configure(text=question_data["question"])

            for i, option in enumerate(question_data["options"]):
                self.answer_buttons[i].configure(text=option, state="normal")

            self.next_button.configure(state="disabled")
        else:
            self.show_results()

    def check_answer(self, selected_index):
        """Verifica si la respuesta seleccionada es correcta."""
        question_data = self.questions[self.current_question_index]
        correct_answer = question_data["answer"]

        if question_data["options"][selected_index] == correct_answer:
            self.score += 1
            print("Respuesta correcta!")
        else:
            print("Respuesta incorrecta!")

        # Desactivar botones de respuesta
        for button in self.answer_buttons:
            button.configure(state="disabled")

        # Habilitar el botón Siguiente
        self.next_button.configure(state="normal")

    def next_question(self):
        """Avanza a la siguiente pregunta."""
        self.current_question_index += 1
        self.show_question()

    def show_results(self):
        """Muestra los resultados finales."""
        result_text = (
            f"¡Quiz completado!\nTu puntuación: {self.score}/{len(self.questions)}"
        )
        self.question_label.configure(text=result_text)

        for button in self.answer_buttons:
            button.pack_forget()  # Ocultar botones de respuesta

        self.next_button.configure(text="Reiniciar", command=self.restart_quiz)

    def restart_quiz(self):
        """Reinicia el quiz."""
        self.current_question_index = 0
        self.score = 0

        for button in self.answer_buttons:
            button.pack(pady=5, fill="x", padx=20)  # Mostrar botones de respuesta

        self.next_button.configure(text="Siguiente", command=self.next_question)
        self.show_question()


if __name__ == "__main__":
    # Configurar CustomTkinter
    ctk.set_appearance_mode("Dark")  # Modes: "System" (default), "Dark", "Light"
    ctk.set_default_color_theme(
        "blue"
    )  # Themes: "blue" (default), "green", "dark-blue"

    # Crear la ventana principal
    root = ctk.CTk()
    app = QuizApp(root)
    root.mainloop()
