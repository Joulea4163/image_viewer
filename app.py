from config import *
import config as local
from view.view_login import ViewLogin as view_login

class app():
    def __init__(self):
        self.root = CTk()
        util_window.load_icon(self.root)
        self.app_login()
        self.root.mainloop()

    def app_login(self):
        view_login(self.root)
    
if __name__ == "__main__":
    app()
