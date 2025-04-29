# Importaciones de configuraciones y vistas necesarias
from config import *  # Importa todo desde el archivo de configuración
import config as local  # Importa el archivo de configuración con un alias
from view.view_image import AnotherWindow  # Importa la vista de imágenes
from view.view_login import ViewLogin  # Importa la vista de login
from tkinter import filedialog  # Importa el módulo de diálogo de archivos de Tkinter

# Clase que define la vista principal del lobby
class LobbyView:
    def init(self, root: CTkToplevel | CTk):  # Constructor (¡hay un error! debería ser _init_ con doble guion bajo)
        self.root = root
        self.main_root = root
        util_window.clear_window(self, self.root)  # Limpia la ventana antes de cargar el lobby
        self.root.title("Lobby")  # Título de la ventana
        self.setup_lobby()  # Configura los elementos del lobby
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)  # Define qué pasa al cerrar la ventana

    # Configura los elementos gráficos del lobby
    def setup_lobby(self):
        self.root.geometry("750x500")  # Tamaño de la ventana
        # Barra superior (tipo menú)
        frame_top = CTkMenuBar(self.root, bg_color="#256CA9", height=25)
        frame_top.pack(fill="x")\
        # Barra inferior con versión y usuario
        bottom_bar = CTkFrame(self.root, fg_color="#256CA9")
        bottom_bar.pack(side=BOTTOM, fill=X)
        version_label = CTkLabel(bottom_bar, text=f"Version:{project_version}", anchor="w")
        version_label.pack(side=LEFT, padx=10)
        user_label = CTkLabel(bottom_bar, text=f"User:{validated_user}", anchor="e")
        user_label.pack(side=RIGHT, padx=10)

        # Contenedor principal para el contenido del lobby
        self.container = CTkFrame(self.root, fg_color="transparent", corner_radius=25, width=1500, height=1500)
        self.container.pack_propagate(False)
        self.container.pack(fill=BOTH, expand=True, padx=10, pady=10)

        # Menú desplegable "Archive"
        menu = frame_top.add_cascade(text="Archive")
        archive_options = CustomDropdownMenu(widget=menu, corner_radius=15)

        # Opciones del menú Archive
        archive_options.add_option(image=local._icon_btn_new, option="New", command=self.create_image_view)
        archive_options.add_option(image=local._icon_btn_open, option="Open", command=self.open_images)
        archive_options.add_option(image=local._icon_btn_save, option="Save")  # Sin función asociada aún
        archive_options.add_option(image=local._icon_btn_logout, option="Logout", command=self.delayed_logout)
        archive_options.add_option(image=local._icon_btn_exit, option="Exit", command=self.on_close)

    # Acción para cerrar sesión (regresar a la vista de login)
    def delayed_logout(self):
        try:
            ViewLogin(self.root)  # Abre la vista de login
        except Exception as e:
            print(f"Error al ejecutar delayed logout: {e}")

    # Abre imágenes seleccionadas por el usuario
    def open_images(self):
        path = filedialog.askopenfilenames(filetypes=local._extensions_list)
        print("path", path)
        if not path in ["", []]:  # Si se seleccionaron archivos
            new_view = CTkToplevel(self.root)  # Nueva ventana para mostrar imágenes
            AnotherWindow(new_view, path)
        else:  # Si no se seleccionaron archivos
            _status_continue = False
            alert = mbox(master=self.root, title="Warning", icon="warning",
                         message="No files selected for show", option_1="ok")
            if alert.get() == "ok":
                pass  # Solo muestra el mensaje

    # Crea una nueva vista con las imágenes seleccionadas
    def create_image_view(self):
        path = filedialog.askopenfilenames(filetypes=local._extensions_list)
        if not path == []:
            new_view = CTkToplevel(self.root)
            AnotherWindow(new_view, path)

    # Acción al cerrar la ventana del lobby
    def on_close(self):
        self.main_root.deiconify()  # Vuelve a mostrar la ventana principal (por si estaba oculta)
        self.root.destroy()  # Cierra la ventana actual