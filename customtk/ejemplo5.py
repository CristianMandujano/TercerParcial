import customtkinter
from PIL import Image

class ToplevelWindow(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("400x300")
        
        # Carga de la imagen
        self.my_image = customtkinter.CTkImage(
            light_image=Image.open("UDL.png"),
            dark_image=Image.open("UDL.png"),
            size=(100, 50)
        )

        self.label = customtkinter.CTkLabel(self, text="ToplevelWindow")
        self.label.pack(padx=20, pady=20)

        self.image_label = customtkinter.CTkLabel(self, image=self.my_image, text="")
        self.image_label.pack(padx=20, pady=20)

class App(customtkinter.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("500x400")

        self.button_1 = customtkinter.CTkButton(self, text="Open Toplevel", command=self.open_toplevel)
        self.button_1.pack(padx=20, pady=20)

        self.toplevel_window = None

    def open_toplevel(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = ToplevelWindow(self)  # Crea la ventana si no existe
        else:
            self.toplevel_window.focus()  # Si ya existe, le da el foco

if __name__ == "__main__":
    app = App()
    app.mainloop()