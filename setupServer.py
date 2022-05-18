import os
import sys

os.environ['TCL_LIBRARY'] = 'tcl86t.dll'
os.environ['TK_LIBRARY'] = 'tk86t.dll'
from cx_Freeze import setup, Executable

base = None
if sys.platform == "win32":  
    base = "Win32GUI"  

executables = [Executable("Server.py", base=base, icon="Alert.ico")]

packages = ["idna", "base64","MainWindow", "table", "os", "PyQt5.QtCore", "PyQt5.QtGui", "PyQt5.QtWidgets", "socket", "threading", "winsound", "time", "configparser", "datetime", "subprocess","plotly","numpy", "cv2", "imutils","hashlib","webbrowser","smtplib","ssl","PIL","json","Cryptodome", "login_class","table_db"]
# addtional_mods = ['numpy.core._methods', 'numpy.lib.format', 'tkinter.filedialog']
options = {
    'build_exe': {
        'packages': packages, "include_files": ["tcl86t.dll", "tk86t.dll"]
        
    },

}

setup(
    name = "Server",
    options = options,
    version = "1.1",
    description = 'The server of the Alert app',
    executables = executables
)