import tkinter as tk
from tkinter import ttk, messagebox
from genetico import algoritmo_genetico
import math
import importlib

def ejecutar_algoritmo():
    try:
        tamaño = int(entry_poblacion.get())
        umbral = float(entry_umbral.get())
        iteraciones = int(entry_iteraciones.get())
        mutacion = float(entry_mutacion.get())
        modo = opcion_funcion.get()
        dimension = 1 if modo == "funcion1" else 2

        if modo == "personalizada":
            expr = entry_personalizada.get()
            def fitness(ind):
                try:
                    x = ind[0]
                    if dimension == 2:
                        x, y = ind
                        return eval(expr, {"math": math, "x": x, "y": y})
                    return eval(expr, {"math": math, "x": x})
                except:
                    return float("-inf")
        else:
            mod = importlib.import_module(f"funciones.{modo}")
            fitness = mod.fitness

        text_salida.delete("1.0", tk.END)
        def log(iteracion, max_fit, med_fit, min_fit):
            text_salida.insert(tk.END, f"Iter {iteracion}: Max={max_fit:.5f}, Med={med_fit:.5f}, Min={min_fit:.5f}\n")
            text_salida.see(tk.END)

        mejor, valor = algoritmo_genetico(
            fitness, dimension, (-10, 10), tamaño, umbral, iteraciones, mutacion, log
        )

        text_salida.insert(tk.END, f"\nÓptimo encontrado: {mejor} con valor {valor:.5f}\n")

    except Exception as e:
        messagebox.showerror("Error", str(e))

# Interfaz gráfica
root = tk.Tk()
root.title("Algoritmo Genético - Interfaz")

frame = ttk.Frame(root, padding=10)
frame.grid()

ttk.Label(frame, text="Tamaño de población:").grid(column=0, row=0)
entry_poblacion = ttk.Entry(frame)
entry_poblacion.insert(0, "10")
entry_poblacion.grid(column=1, row=0)

ttk.Label(frame, text="Umbral diferencia:").grid(column=0, row=1)
entry_umbral = ttk.Entry(frame)
entry_umbral.insert(0, "0.05")
entry_umbral.grid(column=1, row=1)

ttk.Label(frame, text="Iteraciones máximas:").grid(column=0, row=2)
entry_iteraciones = ttk.Entry(frame)
entry_iteraciones.insert(0, "500")
entry_iteraciones.grid(column=1, row=2)

ttk.Label(frame, text="Mutación (variabilidad):").grid(column=0, row=3)
entry_mutacion = ttk.Entry(frame)
entry_mutacion.insert(0, "1")
entry_mutacion.grid(column=1, row=3)

ttk.Label(frame, text="Función:").grid(column=0, row=4)
opcion_funcion = tk.StringVar(value="funcion1")
combo_funciones = ttk.Combobox(frame, textvariable=opcion_funcion)
combo_funciones["values"] = ("funcion1", "funcion2", "personalizada")
combo_funciones.grid(column=1, row=4)

ttk.Label(frame, text="(si eliges personalizada):").grid(column=0, row=5)
entry_personalizada = ttk.Entry(frame, width=40)
entry_personalizada.insert(0, "math.sin(x)**2 / x")
entry_personalizada.grid(column=1, row=5)

btn = ttk.Button(frame, text="Ejecutar", command=ejecutar_algoritmo)
btn.grid(column=0, row=6, columnspan=2, pady=10)

text_salida = tk.Text(frame, height=15, width=60)
text_salida.grid(column=0, row=7, columnspan=2)

root.mainloop()
