import customtkinter as ctk
from tkinter import messagebox
from PIL import Image

class MaquinaRefrescos(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Maquina expendedora de refrescos")
        self.geometry("400x600")
        
        self.saldo = 0.0
        self.precios = {
            "CocaCola": 8, "Fanta": 5, "Sprite": 5,
            "SidralAga": 4, "Jarrito": 5, "Mundet": 4
        }
        self.seleccion = ctk.StringVar(value="None")

        self.menu_frame = ctk.CTkFrame(self, height=30, corner_radius=0)
        self.menu_frame.pack(fill="x", side="top")
        
        self.btn_surtir = ctk.CTkButton(self.menu_frame, text="Surtir", width=60, fg_color="transparent", text_color="white")
        self.btn_surtir.pack(side="left", padx=5)
        
        self.btn_precio = ctk.CTkButton(self.menu_frame, text="Cambiar Precio", width=100, fg_color="transparent", text_color="white")
        self.btn_precio.pack(side="left", padx=5)

        self.lbl_instruccion = ctk.CTkLabel(self, text="0.5, 1, 2, 5, 10", font=("Arial", 14, "bold"))
        self.lbl_instruccion.place(x=20, y=50)

        self.entry_dinero = ctk.CTkEntry(self, width=100)
        self.entry_dinero.place(x=150, y=50)

        self.lbl_total = ctk.CTkLabel(self, text="$ 0.0", font=("Arial", 14, "bold"))
        self.lbl_total.place(x=270, y=50)

        self.btn_ingresar = ctk.CTkButton(self, text="Ingresar", command=self.ingresar_dinero, width=100)
        self.btn_ingresar.place(x=50, y=90)

        self.lbl_precio_tag = ctk.CTkLabel(self, text="Precio : $", font=("Arial", 14, "bold"))
        self.lbl_precio_tag.place(x=180, y=90)
        
        self.lbl_precio_val = ctk.CTkLabel(self, text="0", font=("Arial", 14, "bold"))
        self.lbl_precio_val.place(x=250, y=90)

        self.lbl_cambio = ctk.CTkLabel(self, text="Cambio : $ 0.0", font=("Arial", 14))
        self.lbl_cambio.place(x=120, y=130)

        self.refrescos_frame = ctk.CTkFrame(self, width=350, height=350)
        self.refrescos_frame.place(x=25, y=170)

        ctk.CTkLabel(self.refrescos_frame, text="Refrescos", font=("Arial", 16, "bold")).place(x=20, y=10)

        y_pos = 50
        for nombre, precio in self.precios.items():
            rb = ctk.CTkRadioButton(
                self.refrescos_frame, 
                text=f"{nombre}", 
                variable=self.seleccion, 
                value=nombre,
                command=self.actualizar_vista 
            )
            rb.place(x=30, y=y_pos)
            
            lbl_p = ctk.CTkLabel(self.refrescos_frame, text=str(precio), font=("Arial", 14, "bold"))
            lbl_p.place(x=130, y=y_pos)
            y_pos += 40

        self.canvas_output = ctk.CTkLabel(self.refrescos_frame, text="", width=120, height=200, fg_color="gray30")
        self.canvas_output.place(x=200, y=50)

        self.btn_tomar = ctk.CTkButton(self.refrescos_frame, text="Tomar Refresco", command=self.comprar)
        self.btn_tomar.place(x=100, y=300)

    def actualizar_vista(self):
        bebida = self.seleccion.get()
        
        precio = self.precios[bebida]
        self.lbl_precio_val.configure(text=str(precio))

        try:
            ruta = f"ImagenesMaquina/{bebida}.jpeg"
            img_pil = Image.open(ruta)
            ctk_img = ctk.CTkImage(light_image=img_pil, dark_image=img_pil, size=(110, 180))
            
            self.canvas_output.configure(image=ctk_img, text="")
            self.canvas_output.image = ctk_img 
        except Exception as e:
            self.canvas_output.configure(image=None, text="Error Imagen")
            print(f"Error: {e}")

    def ingresar_dinero(self):
        try:
            monto = float(self.entry_dinero.get())
            if monto in [0.5, 1, 2, 5, 10]:
                self.saldo += monto
                self.lbl_total.configure(text=f"$ {self.saldo}")
                self.entry_dinero.delete(0, 'end')
            else:
                messagebox.showwarning("Moneda no válida", "Solo acepta: 0.5, 1, 2, 5, 10")
        except ValueError:
            messagebox.showerror("Error", "Ingresa un número válido")

    def comprar(self):
        refresco = self.seleccion.get()
        if refresco == "None":
            messagebox.showwarning("Atención", "Selecciona un refresco")
            return
            
        precio = self.precios[refresco]
        if self.saldo >= precio:
            cambio = self.saldo - precio
            self.lbl_cambio.configure(text=f"Cambio : $ {cambio}")
            messagebox.showinfo("Éxito", f"Disfruta tu {refresco}\nTu cambio es: ${cambio}")
            self.saldo = 0
            self.lbl_total.configure(text="$ 0.0")
            self.canvas_output.configure(image=None, text="")
        else:
            messagebox.showerror("Saldo insuficiente", "No ajustas mijo")

if __name__ == "__main__":
    app = MaquinaRefrescos()
    app.mainloop()



