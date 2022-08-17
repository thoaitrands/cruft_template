print("THIS IS A HOOKS")

import os
import shutil

print(os.getcwd())

def remove(filepath):
    print("filepath = " + filepath)
    if os.path.isfile(filepath):
        os.remove(filepath)
    elif os.path.isdir(filepath):
        shutil.rmtree(filepath)

if "{{ cookiecutter.enable_windows }}".lower() == "n":
    remove("windows_configs")