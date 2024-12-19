from config import *
import config as local

class main():
    def __init__(self):
        local._message = "no local"
        self.print_message()

    def print_message(self):
        local._message = local._message + f":Si o {local._message}"
        local._message = local._message + ":Si o {1},{0}".format(local._message,"I don't know")
        print(local._message)

class main_root():
    def __init__(self):
        self.root = CTk()
        util_function.print_message("message from main_root class")
        self.root.mainloop()

#main.message()
if __name__ == "__main__":
    main_root()