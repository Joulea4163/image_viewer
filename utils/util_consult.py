from config import *
import config as local

class util_consult:
    def consult_validate_user(self, user:str, password:str):
        try:
            if user == "nose" and  password == "1234":
                return True
            else:
                return False
        except Exception as ex:
            print(ex)
