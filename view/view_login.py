from config import *
import config as local
import sys
from utils.util_window import util_window as util_window
from utils.util_consult import util_consult as util_consult

class CustomDialog(CTkToplevel):
    def __init__(self,parent,title,message):
        super().__init__(parent)
        self.title(title)
        self.geometry("165x125")
        self.resizable(False,False)

        CTkLabel(self,text=message,font=("Arial",14)).pack(pady=20)
        CTkButton(self,text="OK",command=self.destroy).pack(pady=10)

class ViewLogin:
    def __init__(self,root: CTk|CTkToplevel):
        self.root=root
        util_window.clear_window(self,self.root)
        self.root.title("Login")
        util_window.window_dimentions(self,self.root,115,350,False)
        self.load_resources()
        self.create_widgets()

    def load_resources(self):
        self.model_user=StringVar()
        self.model_password=StringVar()

    def exit_event(self):
        sys.exit(self.root)

    def toggle_password_visibility(self):
        if self.entry_password.cget("show")=="*":
            self.entry_password.configure(show="")
            self.checkbtn_show.select()
        else:
            self.entry_password.configure(show="*")
            self.checkbtn_show.deselect()

    def log_in(self):
        username=self.model_user.get()
        password=self.model_password.get()
        if username=="":
            mbox(master=self.root,
         title="Warning",
         icon="warning",
         message="user is required")
        elif password=="":
            mbox(master=self.root,
         title="Warning",
         icon="warning",
         message="Password is required")
        else:
            status_user=util_consult.consult_validate_user(self,username,password)
            if status_user:
                CustomDialog(self.root,"Info","User valid")
                from view.view_lobby import LobbyView
                LobbyView(self.root)
            else:
                self.model_user.set("")
                self.model_password.set("")
                mbox(master=self.root,
            title="Warning",
            icon="warning",
            message="User or password is incorrect")

    def create_widgets(self):
        CTkLabel(self.root,text="User",font=("Arial",12)).place(x=15,y=5)
        self.entry_name=CTkEntry(self.root,textvariable=self.model_user,font=("Arial",12))
        self.entry_name.place(x=110,y=5)
        self.entry_name.bind("<Return>", lambda event: self.entry_password.focus())

        CTkLabel(self.root,text="Password",font=("Arial",12)).place(x=15,y=35)
        self.entry_password=CTkEntry(self.root,textvariable=self.model_password,font=("Arial",12),show="*")
        self.entry_password.place(x=110,y=35)
        self.entry_password.bind("<Return>",lambda despejar: self.log_in())

        self.checkbtn_show=CTkCheckBox(self.root,text=" ",command=self.toggle_password_visibility,width=15)
        self.checkbtn_show.place(x=295,y=38)

        CTkButton(
            self.root,
            image=local._icon_btn_start,
            compound="left",
            text="Start",
            command=self.log_in,
            font=("Arial",12),
            width=120
        ).place(x=32,y=75)

        CTkButton(
            self.root,
            image=local._icon_btn_cancel,
            compound="left",
            text="Cancel",
            command=self.exit_event,
            font=("Arial",12),
            width=120
        ).place(x=185,y=75)

        self.root.after(100,lambda:self.entry_name.focus())