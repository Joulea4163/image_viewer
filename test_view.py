# Importa todo desde config (posiblemente variables como rutas, íconos, etc.)
from config import *

# Importa config también como un alias 'local' (para acceder como local.algo)
import config as local

# Importa la clase LobbyView desde view.view_lobby y la renombra como 'view'
from view.view_lobby import LobbyView as view
# También hay una vista alternativa comentada (posiblemente para pruebas):
# from view.view_image import AnotherWindow as view

# Define la clase principal de la aplicación
class app():
    def __init__(self):
        # Crea la ventana principal usando customtkinter
        self.root = CTk()
        
        # Carga el ícono de la ventana usando una utilidad externa
        util_window.load_icon(self.root)
        
        # Llama al método que carga la vista principal
        self.app_view()
        
        # Inicia el bucle principal de la aplicación (ventana gráfica)
        self.root.mainloop()

    # Método que carga la vista principal (el LobbyView o la vista de imagen si se cambia la importación)
    def app_view(self):
        view(self.root)

# Punto de entrada principal del programa
if __name__ == "__main__":
    app()
