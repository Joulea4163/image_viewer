# Importaciones necesarias
from config import *  # Importa todas las configuraciones generales
import config as local  # Alias para acceder a variables específicas de configuración
from view.view_login import ViewLogin as view_login  # Importa y renombra la clase de la vista de login

# Clase principal que representa la aplicación completa
class app():
    def __init__(self):
        self.root = CTk()  # Crea la ventana principal usando customtkinter
        util_window.load_icon(self.root)  # Carga el ícono de la aplicación
        self.app_login()  # Lanza la vista de login
        self.root.mainloop()  # Inicia el bucle principal de la interfaz gráfica

    # Método para preparar rutas temporales que usará la app (aunque no se usa en este código actualmente)
    def get_local_data(self):
        # Crea rutas temporales usando el nombre del proyecto
        local.app_path_temp = os.path.join(os.environ['TEMP'], local.project_name)
        local.app_path_temp_view = os.path.join(local.app_path_temp, "views")
        local.app_path_temp_log = os.path.join(local.app_path_temp, "temp")
        local.app_path_temp_log_txt = os.path.join(local.app_path_temp_log, "log.txt")

    # Método para iniciar la vista de login
    def app_login(self):
        view_login(self.root)

# Punto de entrada principal de la aplicación
if __name__ == "__main__":
    app()  # Instancia y ejecuta la aplicación
