from config import *
import config as local
from view.view_image import AnotherWindow
from view.view_login import ViewLogin

class LobbyView:
    def __init__(self, root: CTkToplevel | CTk):
        self.root = root
        self.main_root = root
        util_window.clear_window(self,self.root)
        self.root.title("Lobby")
        self.setup_lobby()
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

    def setup_lobby(self):
        self.root.geometry("750x500")

        frame_top = CTkMenuBar(self.root,bg_color= "#256CA9" , height=25)
        frame_top.pack(fill="x")

        bottom_bar = CTkFrame(self.root,fg_color= "#256CA9")
        bottom_bar.pack(side=BOTTOM, fill=X)
        version_label = CTkLabel(bottom_bar,text=f"Version: {project_version}", anchor="w")
        version_label.pack(side=LEFT, padx=10)
        user_label = CTkLabel(bottom_bar, text=f"User: {validated_user}", anchor="e")
        user_label.pack(side=RIGHT, padx=10)

        self.container = CTkFrame(self.root,fg_color="transparent", corner_radius=25, width=1500, height=1500)
        self.container.pack_propagate(0)
        self.container.pack(fill="both", expand=True, padx=10, pady=10)
        labelLB = CTkLabel(self.root, text="Welcome to the Lobby!", font=("Arial", 16))
        labelLB.pack(pady=50)
        
        menu= frame_top.add_cascade(text="archive")
        archive_options = CustomDropdownMenu(widget=menu, corner_radius = 10)
        archive_options.add_option("new",local._icon_btn_new,command=self.create_image_view)
        archive_options.add_option("open",local._icon_btn_open,command=self.open_images)
        archive_options.add_option("save",local._icon_btn_save)
        archive_options.add_option("logout",local._icon_btn_logout,command=lambda : ViewLogin(self.root))
        archive_options.add_option("exit",local._icon_btn_exit,command=self.on_close)
  
    def open_images(self):
        path = filedialog.askopenfilenames(filetypes=local._extensions_list)
        #AnotherWindow(self.container,path)
        new_view = CTkToplevel(self.root)
        AnotherWindow(new_view,path)

    def create_image_view(self):
        path = filedialog.askopenfilenames(filetypes=local._extensions_list)
        new_view = CTkToplevel(self.root)
        AnotherWindow(new_view,path)

    def on_close(self):
        self.main_root.deiconify()
        self.root.destroy()
