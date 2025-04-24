from CTkMenuBar import *
from customtkinter import *
from PIL import Image,ImageTk
from tkcalendar import Calendar
from utils.util_window import util_window
from utils.util_consult import util_consult
from CTkListbox import CTkListbox as Listbox
from utils.util_function import util_function,viewer_functions
from CTkMessagebox import CTkMessagebox as mbox
from concurrent.futures import ThreadPoolExecutor
from PyPDF2 import PdfFileReader,PdfFileWriter,PdfFileMerger

import fitz
import win32print
import os,sys
import tempfile
import subprocess

project_name="App_View_image"
project_version="0.9.3.0"

app_path_print=os.path.join(".//assets","print","SumatraPDF.exe")
app_path_temp=""
app_path_temp_view=""
app_path_temp_log=""
app_path_temp_log_txt=""


_extensions_list=[("PDF","*.pdf*"),("image","*.png*" ),("image","*.jpg*"),("image","*.ico*"),("image","*.icns*"),("image","*.gif*"),("image","*.webP*"),("image","*.PPM*")]
_photo_lobby=""
_icon_default =""
_icon_window=""
_icon_btn_start=""
_icon_btn_cancel=""
_icon_btn_left=""
_icon_btn_right=""
_icon_btn_zoomin=""
_icon_btn_zoomout=""
_icon_btn_logout=""
_icon_btn_new=""
_icon_btn_open=""
_icon_btn_print=""
_icon_btn_save=""
_icon_btn_exit=""
_icon_test_canva=""


validated_user = "admin"
