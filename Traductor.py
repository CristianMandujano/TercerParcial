import tkinter as tk
from tkinter import messagebox

ARCHIVO = "diccionario.txt"

def registrar_palabra():
    ing = entrada_ing.get().lower().strip()
    esp = entrada_esp.get().lower().strip()
    
    if not ing or not esp:
        messagebox.showwarning("Error", "Llena ambos campos")
        return

    with open(ARCHIVO, "a", encoding="utf-8") as f:
        f.write(f"{ing}:{esp}\n")
    
    messagebox.showinfo("Éxito", "Palabra guardada")
    entrada_ing.delete(0, tk.END)
    entrada_esp.delete(0, tk.END)

def buscar_traduccion(Palabra):
    buscar = entrada_busqueda.get().lower().strip()
    
    try:
        with open(ARCHIVO, "r", encoding="utf-8") as f:
            lineas = f.readlines() 
            
        encontrado = False
        for linea in lineas:
            datos = linea.strip().split(":")
            if len(datos) == 2:
                ingles, espanol = datos
                
                if Palabra == "en_es" and ingles == buscar:
                    lbl_resultado.config(text=f"Español: {espanol}", fg="blue")
                    encontrado = True
                    break
                elif Palabra == "es_en" and espanol == buscar:
                    lbl_resultado.config(text=f"Inglés: {ingles}", fg="green")
                    encontrado = True
                    break
        
        if not encontrado:
            lbl_resultado.config(text="No encontrada", fg="red" )
            
    except FileNotFoundError:
        messagebox.showerror("Error", "Registra una palabra primero.")

ventana = tk.Tk()
ventana.title("Traductor")
ventana.geometry("400x450")

tk.Label(ventana, text="Palabra a buscar", font=("Arial", 12, "bold")).pack(pady=10)
entrada_busqueda = tk.Entry(ventana, width=30)
entrada_busqueda.pack()

tk.Label(ventana, text="Traducción: ", font=("Arial", 12, "bold")).pack(pady=10)

f_btns = tk.Frame(ventana)
f_btns.pack(pady=10)
tk.Button(f_btns, text="Ingles-Español", command=lambda: buscar_traduccion("en_es")).grid(row=0, column=0, padx=5)
tk.Button(f_btns, text="Español-Ingles", command=lambda: buscar_traduccion("es_en")).grid(row=0, column=1, padx=5)

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