# Tutorial de CustomTkinter con Ejercicios y Proyecto Final

CustomTkinter es una biblioteca de Python que extiende Tkinter con widgets modernos y personalizables, permitiendo crear interfaces gráficas más atractivas. Este tutorial te guiará desde los conceptos básicos hasta un proyecto final.

## Instalación

Primero, instala CustomTkinter:

```bash
pip install customtkinter
```

## Parte 1: Fundamentos de CustomTkinter

### 1.1 Ventana Básica

```python
import customtkinter as ctk

app = ctk.CTk()
app.title("Mi Primera App")
app.geometry("400x300")

app.mainloop()
```

**Ejercicio 1:** Crea una ventana con título "Hola CustomTkinter" y tamaño 600x400.

### 1.2 Temas y Apariencia

```python
ctk.set_appearance_mode("System")  # "Light", "Dark" o "System"
ctk.set_default_color_theme("blue")  # "green", "dark-blue", etc.

app = ctk.CTk()
# ... resto del código
```

**Ejercicio 2:** Crea una ventana con tema oscuro y color verde.

### 1.3 Widget Básico: Etiqueta

```python
label = ctk.CTkLabel(app, text="¡Bienvenido!", font=("Arial", 24))
label.pack(pady=20)
```

**Ejercicio 3:** Añade una etiqueta con tu nombre en tamaño 30 y color rojo.

## Parte 2: Widgets Comunes

### 2.1 Botones

```python
def button_callback():
    print("Botón presionado")

button = ctk.CTkButton(app, text="Presiona", command=button_callback)
button.pack(pady=10)
```

**Ejercicio 4:** Crea un botón que cambie el texto de una etiqueta cuando se presiona.

### 2.2 Entradas de Texto

```python
entry = ctk.CTkEntry(app, placeholder_text="Escribe algo")
entry.pack(pady=10)

def get_text():
    print(entry.get())# entry.get() obtiene el texto de la entrada
    entry.delete(0, ctk.END)  # Limpia la entrada después de obtener el texto

btn_get = ctk.CTkButton(app, text="Obtener texto", command=get_text)
btn_get.pack()
```

**Ejercicio 5:** Crea una entrada y un botón que muestre el texto en una etiqueta.

### 2.3 Checkbox y Switch

```python
checkbox = ctk.CTkCheckBox(app, text="Acepto los términos")
checkbox.pack(pady=10)

switch = ctk.CTkSwitch(app, text="Modo avanzado")
switch.pack(pady=10)
```

**Ejercicio 6:** Crea un switch que habilite/deshabilite un botón.
Tip: El widget `Button` tiene un método `configure()` que permite cambiar su estado.
Tip: Usa el método `switch.get()` para obtener el estado del switch.
Tip: Usa el método `switch.configure(state="disabled")` para deshabilitar el botón.
Tip: Usa el método `myboton.configure(state="normal")` para habilitar el botón.

## Parte 3: Diseño con Grid

### 3.1 Sistema de Grid

```python
# Widgets en grid
label1 = ctk.CTkLabel(app, text="Fila 0, Col 0")
label1.grid(row=0, column=0, padx=10, pady=10)

label2 = ctk.CTkLabel(app, text="Fila 0, Col 1")
label2.grid(row=0, column=1, padx=10, pady=10)

button = ctk.CTkButton(app, text="Fila 1, Col 0-1")
button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
```

**Ejercicio 7:** Crea un diseño de 3x3 con etiquetas en cada celda.

## Parte 4: Widgets Avanzados

### 4.1 Combobox

```python
options = ["Opción 1", "Opción 2", "Opción 3"]
combobox = ctk.CTkComboBox(app, values=options)
combobox.pack(pady=10)
```

### 4.2 Slider

```python
slider = ctk.CTkSlider(app, from_=0, to=100)
slider.pack(pady=10)
```

**Ejercicio 8:** Crea un slider que actualice una etiqueta con su valor.

## Parte 5: Proyecto Final - Calculadora

```python
import customtkinter as ctk

class CalculatorApp:
    def __init__(self):
        self.app = ctk.CTk()
        self.app.title("Calculadora")
        self.app.geometry("300x400")
        
        # Configurar el grid
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
            row = (i // 4) + 1
            col = i % 4
            btn = ctk.CTkButton(
                self.app, 
                text=text, 
                command=lambda t=text: self.on_button_click(t)
            )
            btn.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)
    
    def on_button_click(self, text):
        if text == "C":
            self.display.delete(0, ctk.END)
        elif text == "=":
            try:
                result = eval(self.display.get())
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
```

**Ejercicios del Proyecto:**
1. Añade un botón para calcular raíz cuadrada
2. Implementa memoria (botones M+, M-, MR)
3. Cambia el diseño para que sea más atractivo
4. Añade un switch para cambiar entre modo claro y oscuro

## Desafíos Adicionales

1. Crea un editor de texto simple con:
   - Barra de menú
   - Cambio de tema
   - Tamaño de fuente ajustable

2. Desarrolla un conversor de unidades (temperatura, longitud, peso)

3. Implementa un juego simple como tres en raya o buscaminas

## Conclusión

CustomTkinter ofrece una excelente manera de crear interfaces modernas en Python. Con este tutorial has aprendido los fundamentos y estás listo para desarrollar tus propias aplicaciones con widgets personalizados y atractivos.

