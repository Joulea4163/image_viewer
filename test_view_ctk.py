import customtkinter
import os
import tkinter as tk


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        
        self.button = customtkinter.CTkButton(
            self,
            text="my button",
            fg_color="transparent",
            command=self.button_callbck
        )
        self.button.pack(padx=20, pady=20)
        
        self.Image_container = customtkinter.CTkCanvas(
            self, bd=0, relief="ridge", 
            width=self.winfo_screenmmwidth(), height=748
        )
        self.Image_container.pack_propagate(0)
        self.Image_container.pack(fill="both", side=customtkinter.LEFT, expand=True)

        self.archi1 = tk.PhotoImage(file="./asset/icon/image/ImagenDePrueva.png")
        self.Image_container.create_image(50, 50, image=self.archi1, anchor="nw")
        self.Image_container.configure(scrollregion=self.Image_container.bbox("all"))
        self.Image_container.update_idletasks()

    def button_callbck(self):
        print("button clicked")

app = App()
app.mainloop()
