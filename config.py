# Importación de librerías externas necesarias para la interfaz y otras funcionalidades
from CTkMenuBar import *  # Menú estilo CustomTkinter
from customtkinter import *  # Componentes personalizados estilo moderno
from PIL import Image, ImageTk  # Para manejar imágenes
from tkcalendar import Calendar  # Calendario para selección de fechas
from utils.util_window import util_window  # Utilidades relacionadas con ventanas
from utils.util_consult import util_consult  # Funciones de consulta de datos
from CTkListbox import CTkListbox as Listbox  # Listbox personalizada para CTk
from utils.util_function import util_function, viewer_functions  # Otras funciones utilitarias
from CTkMessagebox import CTkMessagebox as mbox  # Mensajes emergentes personalizados

# Módulo para ejecutar tareas en segundo plano con múltiples hilos
from concurrent.futures import ThreadPoolExecutor

# Librerías para trabajar con PDF
from PyPDF2 import PdfFileReader, PdfFileWriter, PdfFileMerger
import fitz  # PyMuPDF, para procesamiento de PDF más avanzado

# Librerías del sistema
import win32print  # Para impresión en Windows
import os, sys  # Para manejo de archivos y del sistema operativo
import tempfile  # Para crear archivos temporales
import subprocess  # Para ejecutar comandos del sistema

# Información general del proyecto
project_name = "App_View_image"
project_version = "0.9.4.0"

# Ruta al visor de PDF portable (SumatraPDF)
app_path_print = os.path.join(".//assets", "print", "SumatraPDF.exe")

# Variables de rutas que se llenarán dinámicamente durante la ejecución
app_path_temp = ""
app_path_temp_view = ""
app_path_temp_log = ""
app_path_temp_log_txt = ""

# Lista de extensiones de archivos soportadas (PDF e imágenes)
_extensions_list = [
    ("PDF", "*.pdf*"),
    ("image", "*.png*"),
    ("image", "*.jpg*"),
    ("image", "*.ico*"),
    ("image", "*.icns*"),
    ("image", "*.gif*"),
    ("image", "*.webP*"),
    ("image", "*.PPM*")
]

# Variables para guardar imágenes e íconos que se cargarán más adelante
_photo_lobby = ""
_icon_default = ""
_icon_window = ""
_icon_btn_start = ""
_icon_btn_cancel = ""
_icon_btn_left = ""
_icon_btn_right = ""
_icon_btn_zoomin = ""
_icon_btn_zoomout = ""
_icon_btn_logout = ""
_icon_btn_new = ""
_icon_btn_open = ""
_icon_btn_print = ""
_icon_btn_save = ""
_icon_btn_exit = ""
_icon_test_canva = ""

# Usuario validado por defecto (podría cambiar durante la sesión)
validated_user = "admin"
