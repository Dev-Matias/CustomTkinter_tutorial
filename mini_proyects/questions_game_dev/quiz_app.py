import customtkinter as ctk
from cargar_questions import load_questions, save_results, cargar_respuesta

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz App")
        self.root.geometry("600x400")
        self.root.resizable(False, False)
        self.questions = load_questions()
        self.current_question_index = cargar_respuesta()[0]
        self.score = cargar_respuesta()[0]
        self.respuesta_correcta = cargar_respuesta()[0]
        self.respuesta_incorrecta = cargar_respuesta()[1]
        self.total_preguntas = len(self.questions)
  
        self.create_widgets()
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def create_widgets(self):
        self.title_label = ctk.CTkLabel(
            self.root, text="Bienvenido al Quiz!", font=("Arial", 24, "bold")
        )
        self.title_label.pack(pady=20)

        self.correct_counter_label = ctk.CTkLabel(
            self.root, text=f"Correctas: {self.respuesta_correcta}", font=("Arial", 16)
        )
        self.correct_counter_label.place(x=10, y=10)

        self.incorrect_counter_label = ctk.CTkLabel(
            self.root, text=f"Incorrectas: {self.respuesta_incorrecta}", font=("Arial", 16)
        )
        self.incorrect_counter_label.place(x=490, y=10)

        self.question_label = ctk.CTkLabel(
            self.root, text="", font=("Arial", 18), wraplength=500
        )
        self.question_label.pack(pady=10)

        self.answer_buttons = []
        for i in range(4):
            button = ctk.CTkButton(
                self.root, text="", command=lambda i=i: self.check_answer(i)
            )
            button.pack(pady=5, fill="x", padx=20)
            self.answer_buttons.append(button)

        self.feedback_label = ctk.CTkLabel(
            self.root, text="", font=("Arial", 16)
        )
        self.feedback_label.pack(pady=10)

        self.next_button = ctk.CTkButton(
            self.root, text="Siguiente", command=self.next_question, state="disabled"
        )
        self.next_button.pack(pady=20)
        self.show_question()

    def show_question(self):
        if self.current_question_index < len(self.questions):
            question_data = self.questions[self.current_question_index]
            self.question_label.configure(text=question_data["pregunta"])

            for i, option in enumerate(question_data["opciones"]):
                self.answer_buttons[i].configure(text=option, state="normal")

            self.next_button.configure(state="disabled")
            self.feedback_label.configure(text="")
        else:
            self.show_results()

    def check_answer(self, selected_index):
        question_data = self.questions[self.current_question_index]
        correct_answer = question_data["respuesta_correcta"]

        if question_data["opciones"][selected_index] == correct_answer:
            self.score += 1
            self.respuesta_correcta += 1
            self.feedback_label.configure(text="Respuesta correcta!", text_color="green")
        else:
            self.respuesta_incorrecta += 1
            self.feedback_label.configure(text="Respuesta incorrecta!", text_color="red")

        self.correct_counter_label.configure(text=f"Correctas: {self.respuesta_correcta}")
        self.incorrect_counter_label.configure(text=f"Incorrectas: {self.respuesta_incorrecta}")

        for button in self.answer_buttons:
            button.configure(state="disabled")

        self.next_button.configure(state="normal")

    def next_question(self):
        self.current_question_index += 1
        self.show_question()

    def show_results(self):
        result_text = (
            f"¡Quiz completado!\nTu puntuación: {self.score}/{len(self.questions)}"
        )
        self.question_label.configure(text=result_text)

        for button in self.answer_buttons:
            button.pack_forget()
        self.next_button.configure(text="Reiniciar", command=self.restart_quiz)

    def restart_quiz(self):
        self.current_question_index = 0
        self.score = 0
        self.respuesta_correcta = 0
        self.respuesta_incorrecta = 0
        save_results(self)

        for button in self.answer_buttons:
            button.pack(pady=5, fill="x", padx=20)

        self.next_button.configure(text="Siguiente", command=self.next_question)
        self.show_question()

    def on_closing(self):
        self.confirm_dialog = ctk.CTkToplevel(self.root)
        self.confirm_dialog.title("Confirmar salida")
        self.confirm_dialog.geometry("300x150")

        confirm_label = ctk.CTkLabel(
            self.confirm_dialog, text="¿Estás seguro de que quieres salir?", font=("Arial", 16)
        )
        confirm_label.pack(pady=20)

        confirm_button = ctk.CTkButton(
            self.confirm_dialog, text="Sí", command=self.confirm_exit
        )
        confirm_button.pack(side="left", padx=10, pady=10)

        cancel_button = ctk.CTkButton(
            self.confirm_dialog, text="No", command=self.confirm_dialog.destroy
        )
        cancel_button.pack(side="right", padx=10, pady=10)

    def confirm_exit(self):
        save_results(self)
        self.root.destroy()

if __name__ == "__main__":
    ctk.set_appearance_mode("Dark")
    ctk.set_default_color_theme("blue")
    root = ctk.CTk()
    app = QuizApp(root)
    root.mainloop()