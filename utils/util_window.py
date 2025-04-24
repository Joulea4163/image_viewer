from config import *
import config as local

class util_window():
    def window_dimentions(self,window: local.CTk|local.CTkToplevel,height: int=400,width: int=300,state_dimention: bool=True):
        x=int((self.root.winfo_screenwidth()/2)-(width/2))
        y=int((self.root.winfo_screenheight()/2)-(height/2))
        window.geometry(f"{width}x{height}+{x}+{y}")
        window.resizable(state_dimention,state_dimention)

    def window_title(self,window: local.CTk,state_title: bool=True):
        window.title("")

    def generate_icon(self,path_icon:str,width: int=25,height: int=25,color:str=None):
        try:
            if os.path.exists(path_icon):
                image=local.Image.open(path_icon)
            else:
                return local._icon_default
        except:
            try:
                if color==None:
                    color="#ffffff"
                image=local.Image.new("RGB",(1000,1000),color)
            except:
                image=local.Image.open(local.os.path.join("asset","icon","default","none.png"))
        img=image.resize((width,height))
        icon=local.ImageTk.PhotoImage(img)
        return icon

    def clear_window(self,window:local.CTk|local.CTkToplevel|local.CTkFrame):
        for widget in window.winfo_children():
            widget.destroy()

    def load_theme(self):
        path_theme=local.os.path.join("./asset","themes")
        theme_path=local.os.path.join(path_theme,"dark-blue.json")
        self.geometry("400x200")

    def load_icon(self):
        def generate_icon(icon_path):
           img=local.Image.open(icon_path)
           return local.ImageTk.PhotoImage(img)
        path_icons=local.os.path.join("./asset","icon")
        icon_path=local.os.path.join(path_icons,"window","icon_window.ico")
        if os.path.exists(icon_path):
            self.iconbitmap(icon_path)
        if os.path.exists(os.path.join(path_icons,"icon_window.png")):
            icon=generate_icon(local.os.path.join(path_icons,"icon_window.png"))
            self.iconphoto(False,icon)

        local._icon_default=util_window.generate_icon(self,local.os.path.join(path_icons,"default","none.png"))
        local._icon_btn_start=util_window.generate_icon(self,local.os.path.join(path_icons,"icon_btn_start.png"))
        local._icon_btn_cancel=util_window.generate_icon(self,local.os.path.join(path_icons,"icon_btn_cancel.png"))
        local._photo_lobby=util_window.generate_icon(self,local.os.path.join(path_icons,"icon_lobby.png"),300,200)
        local._icon_window=util_window.generate_icon(self,local.os.path.join(path_icons,"icon_window.png"),300,200)
        local._icon_btn_cancel=util_window.generate_icon(self,local.os.path.join(path_icons,"icon_btn_cancel.png"))
        local._icon_btn_left=util_window.generate_icon(self,local.os.path.join(path_icons,"icon_btn_left.png"))
        local._icon_btn_right=util_window.generate_icon(self,local.os.path.join(path_icons,"icon_btn_right.png"))
        local._icon_btn_zoomin=util_window.generate_icon(self,local.os.path.join(path_icons,"icon_btn_zoomin.png"))
        local._icon_btn_zoomout=util_window.generate_icon(self,local.os.path.join(path_icons,"icon_btn_zoomout.png"))
        local._icon_btn_logout=util_window.generate_icon(self,local.os.path.join(path_icons,"icon_btn_logout.png"))
        local._icon_btn_new=util_window.generate_icon(self,local.os.path.join(path_icons,"icon_btn_new.png"))
        local._icon_btn_open=util_window.generate_icon(self,local.os.path.join(path_icons,"icon_btn_open.png"))
        local._icon_btn_print=util_window.generate_icon(self,local.os.path.join(path_icons,"icon_btn_print.png"))
        local._icon_btn_save=util_window.generate_icon(self,local.os.path.join(path_icons,"icon_btn_save.png"))
        local._icon_btn_exit=util_window.generate_icon(self,local.os.path.join(path_icons,"icon_btn_exit.png"))
