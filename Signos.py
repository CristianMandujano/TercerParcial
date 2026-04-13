import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from datetime import date
#Investigue la libreria de la fecha por que no me salia el calculo jajajjaja

Signoss = ["Raton", "Toro", "Tigre", "Conejo", "Dragon", 
                   "Serpiente", "Caballo", "Cabra", "Mono", "Gallo", "Perro", "Cerdo"]

def imprimir_resultado():
    try:
        nom = ent_nom.get()
        pat = ent_pat.get()
        mat = ent_mat.get()
        sexo = var_sexo.get()
        
        dia = int(ent_dia.get())
        mes = int(ent_mes.get())
        año = int(ent_anio.get())

        hoy = date.today()
        edad = hoy.year - año - ((hoy.month, hoy.day) < (mes, dia))
        indice = (año - 1900) % 12
        Signo_final = Signoss[indice]
        
        nombre_completo = f"{nom} {pat} {mat}"
        texto_final = f"Hola {nombre_completo}\nTienes {edad} años\ntu signo zodiacal\n\nEs {Signo_final.capitalize()}"
        lbl_res_texto.config(text=texto_final)

        ruta = f"imagenesSigno/{Signo_final}.jpeg" 
        img = Image.open(ruta)
        img = img.resize((130, 130)) 
        foto = ImageTk.PhotoImage(img)
        
        lbl_res_img.config(image=foto)
        lbl_res_img.image = foto 

    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa números válidos en la fecha.")
    except FileNotFoundError:
        messagebox.showerror("Error", f"No se encontró el archivo: {Signoss}.jpeg en la carpeta imagenesSigno")
    except Exception as e:
        messagebox.showerror("Error", str(e))

root = tk.Tk()
root.title("Zodiaco")
root.geometry("750x450")

f_izq = tk.Frame(root, padx=20, pady=20)
f_izq.pack(side="left", fill="both")

tk.Label(f_izq, text="Datos Personales", font=("Arial", 11, "bold")).grid(row=0, columnspan=2, pady=10)

tk.Label(f_izq, text="Nombre").grid(row=1, column=0, sticky="w")
ent_nom = tk.Entry(f_izq); ent_nom.grid(row=1, column=1, pady=2)

tk.Label(f_izq, text="Apaterno").grid(row=2, column=0, sticky="w")
ent_pat = tk.Entry(f_izq); ent_pat.grid(row=2, column=1, pady=2)

tk.Label(f_izq, text="Amaterno").grid(row=3, column=0, sticky="w")
ent_mat = tk.Entry(f_izq); ent_mat.grid(row=3, column=1, pady=2)

tk.Label(f_izq, text="Fecha de nacimiento", font=("Arial", 9, "italic")).grid(row=4, columnspan=2, pady=15)
f_fec = tk.Frame(f_izq)
f_fec.grid(row=5, columnspan=2)

tk.Label(f_fec, text="Día").pack(side="left")
ent_dia = tk.Entry(f_fec, width=4); ent_dia.pack(side="left", padx=2)
tk.Label(f_fec, text="Mes").pack(side="left")
ent_mes = tk.Entry(f_fec, width=4); ent_mes.pack(side="left", padx=2)
tk.Label(f_fec, text="Año").pack(side="left")
ent_anio = tk.Entry(f_fec, width=6); ent_anio.pack(side="left", padx=2)

tk.Label(f_izq, text="Sexo").grid(row=6, column=0, sticky="w", pady=10)
var_sexo = tk.StringVar(value="Masculino")
tk.Radiobutton(f_izq, text="Masculino", variable=var_sexo, value="Masculino").grid(row=7, column=0, sticky="w")
tk.Radiobutton(f_izq, text="Femenino", variable=var_sexo, value="Femenino").grid(row=8, column=0, sticky="w")

btn_imp = tk.Button(f_izq, text="imprimir", bg="black", fg="white", font=("Arial", 10, "bold"), width=15, command=imprimir_resultado)
btn_imp.grid(row=9, columnspan=2, pady=30)

tk.Frame(root, width=2, bg="#CCCCCC").pack(side="left", fill="y", pady=30)

f_der = tk.Frame(root, padx=40, pady=40)
f_der.pack(side="right", expand=True, fill="both")

lbl_res_texto = tk.Label(f_der, text="", font=("Arial", 12, "bold"), justify="center")
lbl_res_texto.pack()

lbl_res_img = tk.Label(f_der) 
lbl_res_img.pack(pady=20)

root.mainloop()