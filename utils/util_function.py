from config import *
import config as local

class util_function():
    def print_message(message:str):
        print(message)

    def generate_folder(path):
        try:
            if not local.os.path.exists(path):
                local.os.makedirs(path)
        except Exception as ex:
            print(ex)
    
class viewer_functions(): 
    def create_temp_folder(base_path="temp"):
        """Creates a temporary directory inside the 'temp' folder and returns its path."""
        os.makedirs(base_path, exist_ok=True)
        temp_folder = tempfile.mkdtemp(dir=base_path)
        return temp_folder
