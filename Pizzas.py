import customtkinter as ctk
from tkinter import ttk, messagebox
import os  # Necesario para rutas de archivos

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

# Esto asegura que el archivo se cree en la misma carpeta que el script
ruta_script = os.path.dirname(os.path.abspath(__file__))
Archivo = os.path.join(ruta_script, "Pizzeria.txt")

app = ctk.CTk()
app.geometry("1000x600")
app.title("Pizzería")

tamaño_var = ctk.StringVar(value="")
ingredientes_vars = {
    "Jamon": ctk.IntVar(),
    "Piña": ctk.IntVar(),
    "Champiñones": ctk.IntVar()
}

precios_tamaño = {"Chica": 40, "Mediana": 80, "Grande": 120}
precios_ingredientes = {"Jamon": 10, "Piña": 10, "Champiñones": 10}
ventas = {}

# --- DISEÑO ORIGINAL ---
frame_top = ctk.CTkFrame(app)
frame_top.pack(fill="x", padx=10, pady=5)

entry_nombre = ctk.CTkEntry(frame_top, placeholder_text="Nombre")
entry_nombre.grid(row=0, column=0, padx=5)

entry_direccion = ctk.CTkEntry(frame_top, placeholder_text="Dirección")
entry_direccion.grid(row=0, column=1, padx=5)

entry_telefono = ctk.CTkEntry(frame_top, placeholder_text="Teléfono")
entry_telefono.grid(row=0, column=2, padx=5)

frame_opciones = ctk.CTkFrame(app)
frame_opciones.pack(fill="x", padx=10, pady=5)

frame_tamaño = ctk.CTkFrame(frame_opciones)
frame_tamaño.grid(row=0, column=0, padx=20)
ctk.CTkLabel(frame_tamaño, text="Tamaño Pizza").pack()
ctk.CTkRadioButton(frame_tamaño, text="Chica $40", variable=tamaño_var, value="Chica").pack(anchor="w")
ctk.CTkRadioButton(frame_tamaño, text="Mediana $80", variable=tamaño_var, value="Mediana").pack(anchor="w")
ctk.CTkRadioButton(frame_tamaño, text="Grande $120", variable=tamaño_var, value="Grande").pack(anchor="w")

frame_ing = ctk.CTkFrame(frame_opciones)
frame_ing.grid(row=0, column=1, padx=20)
ctk.CTkLabel(frame_ing, text="Ingredientes").pack()
ctk.CTkCheckBox(frame_ing, text="Jamón $10", variable=ingredientes_vars["Jamon"]).pack(anchor="w")
ctk.CTkCheckBox(frame_ing, text="Piña $10", variable=ingredientes_vars["Piña"]).pack(anchor="w")
ctk.CTkCheckBox(frame_ing, text="Champiñones $10", variable=ingredientes_vars["Champiñones"]).pack(anchor="w")

frame_num = ctk.CTkFrame(frame_opciones)
frame_num.grid(row=0, column=2, padx=20)
ctk.CTkLabel(frame_num, text="Num. de Pizzas").pack()
entry_cantidad = ctk.CTkEntry(frame_num)
entry_cantidad.pack(pady=5)

frame_tabla = ctk.CTkFrame(app)
frame_tabla.pack(fill="both", expand=True, padx=10, pady=5)

tree = ttk.Treeview(frame_tabla, columns=("Tamaño", "Ingredientes", "Cantidad", "Subtotal"), show="headings")
tree.heading("Tamaño", text="Tamaño")
tree.heading("Ingredientes", text="Ingredientes")
tree.heading("Cantidad", text="Num. Pizzas")
tree.heading("Subtotal", text="SubTotal")
tree.pack(fill="both", expand=True)

# --- FUNCIONES ---
def guardar_venta_en_archivo(nombre, total, items):
    try:
        # Usamos encoding='utf-8' para evitar errores con acentos
        with open(Archivo, "a", encoding="utf-8") as f:
            f.write(f"--- VENTA ---\n")
            f.write(f"Cliente: {nombre}\n")
            for item in items:
                f.write(f"Detalle: {item}\n")
            f.write(f"TOTAL: ${total}\n")
            f.write("-" * 25 + "\n")
    except Exception as e:
        messagebox.showerror("Error de Archivo", f"No se pudo escribir: {e}")

def calcular():
    tamaño = tamaño_var.get()
    if tamaño == "": return 0, ""
    base = precios_tamaño[tamaño]
    ingredientes_lista = [ing for ing, var in ingredientes_vars.items() if var.get() == 1]
    extra = len(ingredientes_lista) * 10
    return base + extra, ", ".join(ingredientes_lista)

def agregar():
    try:
        cantidad = int(entry_cantidad.get())
        precio_unitario, ingredientes = calcular()
        if tamaño_var.get() == "":
            messagebox.showwarning("Atención", "Selecciona un tamaño")
            return
        subtotal = precio_unitario * cantidad
        tree.insert("", "end", values=(tamaño_var.get(), ingredientes, cantidad, subtotal))
    except:
        messagebox.showerror("Error", "Cantidad inválida")

def quitar():
    seleccionado = tree.selection()
    if seleccionado: tree.delete(seleccionado)

def terminar():
    total = 0
    items_vendidos = []
    for item in tree.get_children():
        valores = tree.item(item)["values"]
        total += int(valores[3])
        items_vendidos.append(f"{valores[2]} pizza(s) {valores[0]} con {valores[1]}")

    if not items_vendidos:
        messagebox.showwarning("Vacío", "No hay productos en la tabla")
        return

    nombre = entry_nombre.get() or "Cliente"
    ventas[nombre] = ventas.get(nombre, 0) + total
    actualizar_ventas()
    
    # GUARDAR
    guardar_venta_en_archivo(nombre, total, items_vendidos)

    messagebox.showinfo("Total", f"Venta guardada. Total: ${total}")
    for i in tree.get_children(): tree.delete(i)

def actualizar_ventas():
    texto = ""
    total_dia = 0
    for cliente, total in ventas.items():
        texto += f"{cliente} total ${total}\n"
        total_dia += total
    label_ventas.configure(text=texto + f"\nVentas totales del día: ${total_dia}")

frame_botones = ctk.CTkFrame(app)
frame_botones.pack(fill="x", padx=10)
ctk.CTkButton(frame_botones, text="Agregar", command=agregar).pack(side="left", padx=10)
ctk.CTkButton(frame_botones, text="Quitar", command=quitar).pack(side="left", padx=10)
ctk.CTkButton(frame_botones, text="Terminar", command=terminar).pack(side="left", padx=10)

frame_ventas = ctk.CTkFrame(app)
frame_ventas.pack(side="right", fill="y", padx=10, pady=10)
ctk.CTkLabel(frame_ventas, text="Ventas del día").pack()
label_ventas = ctk.CTkLabel(frame_ventas, text="", justify="left")
label_ventas.pack()

app.mainloop()

