from config import *
import config as local

class util_window():
    def window_dimentions(self,window: CTk | local.CTkToplevel, height: int = 400, width: int = 300, state_dimention: bool=True):
        x = int((self.root.winfo_screenwidth()/2)-(width/2))
        y = int((self.root.winfo_screenheight()/2)-(height/2))
        window.geometry(f"{width}x{height}+{x}+{y}")
        window.resizable(state_dimention,state_dimention)

    def window_title(self,window: CTk, state_title: bool=True):
        window.title("")

    def generate_icon(self,path_icon:str, width: int =25, height: int =25):
        try:
            if os.path.exists(path_icon):
                image = local.Image.open(path_icon)

            else:
                print("don't exist")
        except Exception as ex:
            print("Error", str(ex))
        finally:
            img=image.resize((width,height))
            icon=local.ImageTk.PhotoImage(img)
            return icon

    def clear_window(self, window:CTk | local.CTkToplevel | local.CTkFrame):
        for widget in window.winfo_children():
            widget.destroy()

    def load_theme(self):
        path_theme = local.os.path.join("./asset", "themes")
        theme_path = local.os.path.join(path_theme, "dark-blue.json")
        try:
            set_default_color_theme(theme_path)
        except Exception as ex:
            print(ex)
        self.geometry("400x200")

    def load_icon(self):
        def generate_icon(icon_path):
           img = local.Image.open(icon_path)
           return local.ImageTk.PhotoImage(img)
        path_icons = local.os.path.join("./asset", "icon")
        icon_path =  local.os.path.join(path_icons, "window", "icon_window.ico")
        
        self.iconbitmap(icon_path)
        icon = generate_icon(local.os.path.join(path_icons, "icon_window.png"))
        self.iconphoto(False, icon)

        local._icon_btn_start = util_window.generate_icon(self,local.os.path.join(path_icons,"icon_btn_start.png"))
        local._icon_btn_cancel = util_window.generate_icon(self,local.os.path.join(path_icons,"icon_btn_cancel.png"))
        local._photo_lobby = util_window.generate_icon(self,local.os.path.join(path_icons,"image","ImageTest.png"),300,200)
        #image = Image.open(ShowImage)

        local._icon_test_canva = ImageTk.PhotoImage(file="./asset/icon/image/imageTest.png")
