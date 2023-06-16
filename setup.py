import sys
from cx_Freeze import setup, Executable

build_exe_options = {
    "packages": ["numpy", "tkinter", "PIL"],
    "include_files": ["assets", "matrices_guardadas.txt"],
}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="TablaLoteria",
    version="1.0",
    description="Tabla de Lotería",
    options={"build_exe": build_exe_options},
    executables=[Executable("main.py", base=base)],
)
