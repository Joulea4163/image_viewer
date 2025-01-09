from customtkinter import *
from CTkMenuBar import *
from CTkListbox import CTkListbox as Listbox
from tkcalendar import Calendar
import os,sys
from PIL import Image,ImageTk
from CTkMessagebox import CTkMessagebox as mbox
from utils.util_consult import util_consult
from utils.util_window import util_window
from utils.util_function import util_function
from utils.util_data import util_data

import fitz
from PyPDF2 import PdfFileReader, PdfFileWriter, PdfFileMerger

project_name = "App_View_image"
project_version = "0.9.0.0"

app_path_temp = ""
app_path_temp_view = ""
app_path_temp_log = ""
app_path_temp_log_txt = ""


_extensions_list = [("image","*.png*" ), ("image","*.jpg*"), ("image","*.ico*"), ("image","*.icns*"), ("image","*.gif*"), ("image","*.webP*"), ("image","*.PPM*")]
_icon_default =""
_photo_lobby = ""
_icon_window = ""
_icon_btn_start = ""
_icon_btn_cancel = ""
_icon_test_canva = ""



validated_user = "nose"