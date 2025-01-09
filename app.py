from config import *
import config as local
from view.view_login import ViewLogin as view_login

class app():
    def __init__(self):
        self.root = CTk()
        util_window.load_icon(self.root)
        self.app_login()
        self.root.mainloop()

    def get_local_data(self):
        local.app_path_temp=os.path.join(os.environ['TEMP'],local.project_name)
        local.app_path_temp_view=os.path.join(local.app_path_temp,"views")
        local.app_path_temp_log=os.path.join(local.app_path_temp,"temp")
        local.app_path_temp_log_txt=os.path.join(local.app_path_temp_log,"log.txt")
    
    def app_login(self):
        view_login(self.root)
    
if __name__ == "__main__":
    app()
