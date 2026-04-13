import tkinter as tk
from tkinter import messagebox

ARCHIVO = "diccionario.txt"

def registrar_palabra():
    ing = entrada_ing.get().strip()
    esp = entrada_esp.get().strip()
    
    if not ing or not esp:
        messagebox.showwarning("Error", "Llena ambos campos")
        return

    with open(ARCHIVO, "a") as f:
        f.write(f"{ing}:{esp}\n")
    
    messagebox.showinfo("Éxito", "Palabra guardada")
    entrada_ing.delete(0, tk.END)
    entrada_esp.delete(0, tk.END)

def buscar_traduccion():
    modo = opcion_var.get()  
    buscar = entrada_busqueda.get().strip()
    
    if modo == "ninguno":
        messagebox.showwarning("Error", "Selecciona la traducción")
        return

    if not buscar:
        messagebox.showwarning("Error", "Escribe una palabra para buscar")
        return

    try:
        with open(ARCHIVO, "r") as f:
            lineas = f.readlines() 
            
        encontrado = False
        for linea in lineas:
            datos = linea.strip().split(":")
            if len(datos) == 2:
                ingles, espanol = datos

                if modo == "en_es" and ingles.lower() == buscar.lower():
                    lbl_resultado.config(text=f"Español: {espanol}", fg="green")
                    encontrado = True
                    break
                elif modo == "es_en" and espanol.lower() == buscar.lower():
                    lbl_resultado.config(text=f"Inglés: {ingles}", fg="green")
                    encontrado = True
                    break
        
        if not encontrado:
            lbl_resultado.config(text="No encontrada", fg="red")
            
    except FileNotFoundError:
        messagebox.showerror("Error", "El archivo no existe. Registra una palabra primero.")

ventana = tk.Tk()
ventana.title("Traductor")
ventana.geometry("400x550")

opcion_var = tk.StringVar(value="nada")

tk.Label(ventana, text="Palabra a buscar", font=("Arial", 12, "bold")).pack(pady=10)
entrada_busqueda = tk.Entry(ventana, width=30)
entrada_busqueda.pack()

tk.Label(ventana, text="Traducción: ", font=("Arial", 12, "bold")).pack(pady=10)

f_btns = tk.Frame(ventana)
f_btns.pack(pady=10)

tk.Radiobutton(f_btns, text="Ingles-Español", variable=opcion_var, value="en_es").grid(row=0, column=0, padx=5)
tk.Radiobutton(f_btns, text="Español-Ingles", variable=opcion_var, value="es_en").grid(row=0, column=1, padx=5)

tk.Button(ventana, text="Traducir", command=buscar_traduccion).pack(pady=5)

lbl_resultado = tk.Label(ventana, text="", font=("Arial", 12))
lbl_resultado.pack(pady=10)

tk.Label(ventana, text="Registra una nueva palabra", font=("Arial", 12, "bold")).pack(pady=10)
tk.Label(ventana, text="Español:").pack()
entrada_esp = tk.Entry(ventana)
entrada_esp.pack()
tk.Label(ventana, text="Inglés:").pack()
entrada_ing = tk.Entry(ventana)
entrada_ing.pack()

tk.Button(ventana, text="Registrar", command=registrar_palabra).pack(pady=20)

ventana.mainloop()
