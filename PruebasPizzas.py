import customtkinter as ctk
from tkinter import ttk, messagebox
from datetime import datetime

ctk.set_appearance_mode("light")

# VARIABLES

precios = {
    "Chica": 40,
    "Mediana": 80,
    "Grande": 120
}

precios_ing = {
    "Jamón": 10,
    "Piña": 10,
    "Champiñones": 10
}

carrito = []
ventas = {}

# FUNCIONES

def calcular_subtotal():
    tamaño = tamaño_var.get()
    ingredientes = obtener_ingredientes()
    num = int(spin_pizzas.get())

    subtotal = precios[tamaño]
    subtotal += sum(precios_ing[i] for i in ingredientes)
    subtotal *= num

    return subtotal


def obtener_ingredientes():
    ing = []
    if var_jamon.get():
        ing.append("Jamón")
    if var_pina.get():
        ing.append("Piña")
    if var_champ.get():
        ing.append("Champiñones")
    return ing


def agregar():
    try:
        nombre = entry_nombre.get()
        if not nombre:
            raise Exception("Nombre vacío")

        tamaño = tamaño_var.get()
        ingredientes = obtener_ingredientes()
        num = int(spin_pizzas.get())
        subtotal = calcular_subtotal()

        datos = (tamaño, ", ".join(ingredientes), num, subtotal)
        carrito.append(datos)

        tree.insert("", "end", values=datos)

    except:
        messagebox.showerror("Error", "Datos incorrectos")


def quitar():
    seleccionado = tree.selection()
    if not seleccionado:
        return

    for item in seleccionado:
        tree.delete(item)


def terminar():
    nombre = entry_nombre.get()

    if not nombre:
        messagebox.showerror("Error", "Ingresa nombre")
        return

    total = 0
    for item in tree.get_children():
        valores = tree.item(item)["values"]
        total += int(valores[3])

    # Guardar en archivo
    with open("ventas.txt", "a") as f:
        f.write(f"{nombre},{total}\n")

    # Acumular ventas
    if nombre in ventas:
        ventas[nombre] += total
    else:
        ventas[nombre] = total

    mostrar_ventas()

    messagebox.showinfo("Total", f"{nombre} debe pagar: ${total}")

    limpiar()


def mostrar_ventas():
    texto = ""
    total_dia = 0

    for cliente, total in ventas.items():
        texto += f"{cliente} total ${total}\n"
        total_dia += total

    texto += f"\nVentas del día: ${total_dia}"

    label_ventas.configure(text=texto)


def limpiar():
    for item in tree.get_children():
        tree.delete(item)

    entry_nombre.delete(0, "end")
    entry_direccion.delete(0, "end")
    entry_telefono.delete(0, "end")


# INTERFAZ

app = ctk.CTk()
app.title("Sistema Pizzería")
app.geometry("900x500")

# DATOS DEL CLIENTE

frame_top = ctk.CTkFrame(app)
frame_top.pack(fill="x", padx=10, pady=5)

ctk.CTkLabel(frame_top, text="Nombre").grid(row=0, column=0)
entry_nombre = ctk.CTkEntry(frame_top)
entry_nombre.grid(row=0, column=1)

ctk.CTkLabel(frame_top, text="Dirección").grid(row=0, column=2)
entry_direccion = ctk.CTkEntry(frame_top)
entry_direccion.grid(row=0, column=3)

ctk.CTkLabel(frame_top, text="Teléfono").grid(row=0, column=4)
entry_telefono = ctk.CTkEntry(frame_top)
entry_telefono.grid(row=0, column=5)

# TAMAÑO 

frame_opciones = ctk.CTkFrame(app)
frame_opciones.pack(fill="x", padx=10, pady=5)

tamaño_var = ctk.StringVar(value="Chica")

ctk.CTkLabel(frame_opciones, text="Tamaño").grid(row=0, column=0)
ctk.CTkRadioButton(frame_opciones, text="Chica $40", variable=tamaño_var, value="Chica").grid(row=1, column=0)
ctk.CTkRadioButton(frame_opciones, text="Mediana $80", variable=tamaño_var, value="Mediana").grid(row=2, column=0)
ctk.CTkRadioButton(frame_opciones, text="Grande $120", variable=tamaño_var, value="Grande").grid(row=3, column=0)

# INGREDIENTES

var_jamon = ctk.BooleanVar()
var_pina = ctk.BooleanVar()
var_champ = ctk.BooleanVar()

ctk.CTkLabel(frame_opciones, text="Ingredientes").grid(row=0, column=1)

ctk.CTkCheckBox(frame_opciones, text="Jamón $10", variable=var_jamon).grid(row=1, column=1)
ctk.CTkCheckBox(frame_opciones, text="Piña $10", variable=var_pina).grid(row=2, column=1)
ctk.CTkCheckBox(frame_opciones, text="Champiñones $10", variable=var_champ).grid(row=3, column=1)

# NUM PIZZAS 

ctk.CTkLabel(frame_opciones, text="Num. Pizzas").grid(row=0, column=2)
spin_pizzas = ctk.CTkEntry(frame_opciones)
spin_pizzas.insert(0, "1")
spin_pizzas.grid(row=1, column=2)

# BOTON

ctk.CTkButton(frame_opciones, text="Agregar", command=agregar).grid(row=2, column=2)

# TABLA

frame_tabla = ctk.CTkFrame(app)
frame_tabla.pack(fill="both", expand=True, padx=10, pady=5)

tree = ttk.Treeview(frame_tabla, columns=("tamaño", "ingredientes", "num", "subtotal"), show="headings")

tree.heading("tamaño", text="Tamaño")
tree.heading("ingredientes", text="Ingredientes")
tree.heading("num", text="Num")
tree.heading("subtotal", text="Subtotal")

tree.pack(fill="both", expand=True)

# BOTONES

frame_btn = ctk.CTkFrame(app)
frame_btn.pack(fill="x")

ctk.CTkButton(frame_btn, text="Quitar", command=quitar).pack(side="left", padx=10)
ctk.CTkButton(frame_btn, text="Terminar", command=terminar).pack(side="left")

# VENTAS

label_ventas = ctk.CTkLabel(app, text="Ventas del día")
label_ventas.pack(pady=10)

app.mainloop()