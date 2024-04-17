import sys
from cx_Freeze import setup, Executable

build_exe_options = {
    "excludes":[],
    "zip_include_packages":[]
}

setup(
    name="ghostmode",
    version="0.1",
    description="Activate JS8Call GhostMode",
    options={"build_exe":build_exe_options},
    executables=[Executable("ghostmode.py")]
)

