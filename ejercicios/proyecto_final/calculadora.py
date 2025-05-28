import customtkinter as ctk
from math_utils import mr, m_plus, m_minus

class CalculatorApp:
    def __init__(self):
        self.app = ctk.CTk()
        self.app.title("Calculadora")
        self.app.geometry("400x400")
        # Set the default color theme
        ctk.set_appearance_mode("light")  # Modes: "System" (default), "Light", "Dark"
        ctk.set_default_color_theme("dark-blue")  # Themes: "blue" (default), "green", "dark-blue"

        self.app.grid_columnconfigure((0, 1, 2, 3), weight=1)
        self.app.grid_rowconfigure((0, 1, 2, 3, 4), weight=1)
        
        # Pantalla
        self.display = ctk.CTkEntry(self.app, font=("Arial", 24))
        self.display.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=10, pady=10)
        
        # Botones
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '=', '+'
        ]
        
        for i, text in enumerate(buttons):
            row = (i // 4) + 1 # La fila comienza en 1 para dejar espacio para la pantalla
            col = i % 4 # La columna es el resto de la división
            
            btn = ctk.CTkButton(
                self.app, 
                text=text, 
                command=lambda t=text: self.on_button_click(t)
            )# lambda para pasar el texto del botón a la función
            #funcion lambda para evitar que se ejecute al crear el botón
            # y en su lugar se ejecute al hacer clic
            btn.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)
        
        # Botones M+ , M-, MR
        self.memory = 0
        self.memory_label = ctk.CTkButton(self.app, text="MR", command="")
        self.memory_label.grid(row=5, column=0, sticky="nsew", padx=10, pady=10)
        self.btn_m_plus = ctk.CTkButton(self.app, text="M+", command="")
        self.btn_m_plus.grid(row=5, column=1, sticky="nsew", padx=10, pady=10)
        self.btn_m_minus = ctk.CTkButton(self.app, text="M-", command="")
        self.btn_m_minus.grid(row=5, column=2, sticky="nsew", padx=10, pady=10)

        #Cambiar el tema de la calculadora
        def change_theme():
            if self.switch.get() == 1:
                ctk.set_appearance_mode("dark")
                ctk.set_default_color_theme("dark-blue")
                self.switch.configure(text="Dark")
            else:
                ctk.set_appearance_mode("light")
                ctk.set_default_color_theme("blue")
                self.switch.configure(text="Light")
        #Switch para cambiar el tema
        self.switch = ctk.CTkSwitch(self.app, text="Dark", command=change_theme)
        self.switch.grid(row=5, column=3, columnspan=3, sticky="nsew", padx=10, pady=10)
    def on_button_click(self, text):
        print(text)

        if text == "C":
            self.display.delete(0, ctk.END)
        elif text == "=":
            try:
                result = eval(self.display.get())# eval para evaluar la expresión matemática
                # Se recomienda no usar eval en producción
                # debido a problemas de seguridad, pero es útil para este ejemplo
                # y para aprender a usar la calculadora
                # Se puede usar una librería como sympy para evaluar expresiones matemáticas
                # de forma segura
                self.display.delete(0, ctk.END)
                self.display.insert(0, str(result))
            except:
                self.display.delete(0, ctk.END)
                self.display.insert(0, "Error")
        else:
            self.display.insert(ctk.END, text)
    
    def run(self):
        self.app.mainloop()

if __name__ == "__main__":
    calculator = CalculatorApp()
    calculator.run()
