#F3nix
import tkinter as tk
from tkinter import messagebox

# Función para calcular el porcentaje de stop-loss o take-profit y el precio objetivo
def calcular_stop_loss_ganancia(precio_entrada, apalancamiento, porcentaje_real):
    porcentaje_objetivo = porcentaje_real / apalancamiento
    precio_objetivo = precio_entrada * (1 - porcentaje_objetivo / 100)
    return porcentaje_objetivo, precio_objetivo

def calcular_take_profit(precio_entrada, apalancamiento, porcentaje_real):
    porcentaje_objetivo = porcentaje_real / apalancamiento
    precio_objetivo = precio_entrada * (1 + porcentaje_objetivo / 100)
    return porcentaje_objetivo, precio_objetivo

# Función para mostrar los resultados en la interfaz
def calcular():
    try:
        # Obtener datos de entrada
        capital = float(entry_capital.get())
        apalancamiento = float(entry_apalancamiento.get())
        porcentaje_perdida_real = float(entry_perdida_real.get())
        porcentaje_ganancia_real = float(entry_ganancia_real.get())
        precio_entrada = float(entry_precio_entrada.get())

        # Cálculo de stop-loss y take-profit
        porcentaje_stop_loss, precio_stop_loss = calcular_stop_loss_ganancia(precio_entrada, apalancamiento, porcentaje_perdida_real)
        porcentaje_take_profit, precio_take_profit = calcular_take_profit(precio_entrada, apalancamiento, porcentaje_ganancia_real)

        # Cálculo de la ganancia/pérdida en dinero real
        dinero_perdido = capital * (porcentaje_stop_loss / 100) * apalancamiento
        dinero_ganado = capital * (porcentaje_take_profit / 100) * apalancamiento

        # Mostrar los resultados en la interfaz con precisión de 6 decimales
        label_result.config(text=f"Para una pérdida real de {porcentaje_perdida_real}%:\n"
                                 f"Configura el stop-loss en aproximadamente {porcentaje_stop_loss:.6f}% "
                                 f"(Precio objetivo: {precio_stop_loss:.6f})\n"
                                 f"Dinero perdido si se llega a este stop-loss: ${dinero_perdido:.2f}\n\n"
                                 f"Para una ganancia real de {porcentaje_ganancia_real}%:\n"
                                 f"Configura el take-profit en aproximadamente {porcentaje_take_profit:.6f}% "
                                 f"(Precio objetivo: {precio_take_profit:.6f})\n"
                                 f"Dinero ganado si se llega a este take-profit: ${dinero_ganado:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese valores numéricos válidos.")

# Configuración de la ventana principal
root = tk.Tk()
root.title("Calculadora de Apalancamiento")

# Estilizar la ventana principal con un borde 3D
root.configure(bg="#d9e3f0")  # Color de fondo para una apariencia más moderna
root.geometry("450x650")
root.resizable(False, False)  # Fijar tamaño para mayor consistencia visual

# Configuración de estilos de entradas y etiquetas
entry_style = {"bd": 2, "relief": "groove", "font": ("Arial", 12)}
label_style = {"bg": "#d9e3f0", "font": ("Arial", 10, "bold")}
label_result_style = {"bg": "#f5f8fa", "relief": "sunken", "bd": 2, "justify": "left", "wraplength": 420}

# Crear etiquetas y campos de entrada
tk.Label(root, text="Capital invertido (dinero real):", **label_style).pack(pady=5)
entry_capital = tk.Entry(root, **entry_style)
entry_capital.pack(pady=5)

tk.Label(root, text="Porcentaje de apalancamiento:", **label_style).pack(pady=5)
entry_apalancamiento = tk.Entry(root, **entry_style)
entry_apalancamiento.pack(pady=5)

tk.Label(root, text="Porcentaje de pérdida real dispuesto a perder:", **label_style).pack(pady=5)
entry_perdida_real = tk.Entry(root, **entry_style)
entry_perdida_real.pack(pady=5)

tk.Label(root, text="Porcentaje de ganancia real deseado:", **label_style).pack(pady=5)
entry_ganancia_real = tk.Entry(root, **entry_style)
entry_ganancia_real.pack(pady=5)

tk.Label(root, text="Precio de entrada del activo:", **label_style).pack(pady=5)
entry_precio_entrada = tk.Entry(root, **entry_style)
entry_precio_entrada.pack(pady=5)

# Botón para calcular, con un estilo de botón 3D
btn_calcular = tk.Button(root, text="Calcular", command=calcular,
                         font=("Arial", 12, "bold"), bg="#4a90e2", fg="white", bd=5, relief="raised", cursor="hand2")
btn_calcular.pack(pady=20)

# Etiqueta para mostrar los resultados con borde 3D y mayor altura
label_result = tk.Label(root, text="", **label_result_style, font=("Arial", 10), height=12)
label_result.pack(pady=20, padx=10, fill="both")

# Ejecutar la ventana
root.mainloop()
