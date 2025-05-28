import customtkinter as ctk

class BlankSpaceGame(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Blank Space Game")
        self.geometry("600x400")
        
        # Set the default color theme
        ctk.set_appearance_mode("System")  # Modes: "System" (default), "Light", "Dark"
        ctk.set_default_color_theme("blue")  # Themes: "blue" (default), "green", "dark-blue"

        self.create_widgets()

    def create_widgets(self):
        self.label = ctk.CTkLabel(self, text="Blank Space Game!", font=("Arial", 20))
        self.label.pack(pady=20)

        self.start_button = ctk.CTkButton(self, text="Start Game", command=self.start_game)
        self.start_button.pack(pady=10)

    def start_game(self):
        self.label.configure(text="Game Started! Fill in the blanks.")
        # Here you can add more game logic
        self.start_button.configure(state="disabled")
if __name__ == "__main__":
    app = BlankSpaceGame()
    app.mainloop()