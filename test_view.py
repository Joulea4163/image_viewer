from config import *
import config as local
from view.view_lobby import LobbyView as view
#from view.view_image import AnotherWindow as view

class app():
    def __init__(self):
        self.root =CTk()
        util_window.load_icon(self.root)
        self.app_view()
        self.root.mainloop()

    def app_view(self):
        view(self.root)

if __name__ == "__main__":
    app()
