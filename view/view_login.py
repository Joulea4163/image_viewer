# Importaciones necesarias de configuración y utilidades
from config import *
import config as local
import sys
from utils.util_window import util_window as util_window
from utils.util_consult import util_consult as util_consult

# Clase que representa un cuadro de diálogo personalizado tipo modal
class CustomDialog(CTkToplevel):
    def __init__(self, parent, title, message):
        super().__init__(parent)
        self.title(title)  # Título del cuadro de diálogo
        self.geometry("165x125")  # Dimensiones fijas
        self.resizable(False, False)  # Desactiva el redimensionamiento

        # Etiqueta con el mensaje
        CTkLabel(self, text=message, font=("Arial", 14)).pack(pady=20)
        # Botón para cerrar el cuadro de diálogo
        CTkButton(self, text="OK", command=self.destroy).pack(pady=10)

# Clase que define la vista de inicio de sesión (login)
class ViewLogin:
    def __init__(self, root: CTk | CTkToplevel):
        self.root = root
        # Limpia cualquier contenido previo en la ventana
        util_window.clear_window(self, self.root)
        self.root.title("Login")  # Establece el título de la ventana
        # Define las dimensiones de la ventana
        util_window.window_dimentions(self, self.root, 115, 350, False)
        # Carga los recursos (variables) del formulario
        self.load_resources()
        # Crea los widgets (componentes visuales)
        self.create_widgets()

    # Inicializa los modelos de datos (variables ligadas a los campos)
    def load_resources(self):
        self.model_user = StringVar()
        self.model_password = StringVar()

    # Evento para cerrar la aplicación
    def exit_event(self):
        sys.exit(self.root)

    # Alterna la visibilidad de la contraseña (mostrar/ocultar)
    def toggle_password_visibility(self):
        if self.entry_password.cget("show") == "*":
            self.entry_password.configure(show="")  # Muestra la contraseña
            self.checkbtn_show.select()
        else:
            self.entry_password.configure(show="*")  # Oculta la contraseña
            self.checkbtn_show.deselect()

    # Lógica para iniciar sesión
    def log_in(self):
        username = self.model_user.get()
        password = self.model_password.get()

        # Validación básica de campos vacíos
        if username == "":
            mbox(master=self.root, title="Warning", icon="warning", message="user is required")
        elif password == "":
            mbox(master=self.root, title="Warning", icon="warning", message="Password is required")
        else:
            # Valida el usuario con una función de utilidad
            status_user = util_consult.consult_validate_user(self, username, password)
            if status_user:
                # Usuario válido, muestra mensaje y carga nueva vista
                CustomDialog(self.root, "Info", "User valid")
                from view.view_lobby import LobbyView
                LobbyView(self.root)
            else:
                # Usuario inválido, limpia campos y muestra advertencia
                self.model_user.set("")
                self.model_password.set("")
                mbox(master=self.root, title="Warning", icon="warning", message="User or password is incorrect")

    # Crea los elementos gráficos del formulario de login
    def create_widgets(self):
        # Etiqueta y campo para el nombre de usuario
        CTkLabel(self.root, text="User", font=("Arial", 12)).place(x=15, y=5)
        self.entry_name = CTkEntry(self.root, textvariable=self.model_user, font=("Arial", 12))
        self.entry_name.place(x=110, y=5)
        self.entry_name.bind("<Return>", lambda event: self.entry_password.focus())  # Salta al campo contraseña

        # Etiqueta y campo para la contraseña
        CTkLabel(self.root, text="Password", font=("Arial", 12)).place(x=15, y=35)
        self.entry_password = CTkEntry(self.root, textvariable=self.model_password, font=("Arial", 12), show="*")
        self.entry_password.place(x=110, y=35)
        self.entry_password.bind("<Return>", lambda despejar: self.log_in())  # Inicia sesión al presionar Enter

        # CheckBox para mostrar u ocultar la contraseña
        self.checkbtn_show = CTkCheckBox(self.root, text=" ", command=self.toggle_password_visibility, width=15)
        self.checkbtn_show.place(x=295, y=38)

        # Botón para iniciar sesión
        CTkButton(
            self.root,
            image=local._icon_btn_start,
            compound="left",
            text="Start",
            command=self.log_in,
            font=("Arial", 12),
            width=120
        ).place(x=32, y=75)

        # Botón para cancelar (cerrar aplicación)
        CTkButton(
            self.root,
            image=local._icon_btn_cancel,
            compound="left",
            text="Cancel",
            command=self.exit_event,
            font=("Arial", 12),
            width=120
        ).place(x=185, y=75)

        # Coloca el foco inicial en el campo de usuario
        self.root.after(100, lambda: self.entry_name.focus())
