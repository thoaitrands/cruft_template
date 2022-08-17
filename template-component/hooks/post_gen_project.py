print("THIS IS A HOOKS")

import os
import shutil

print(os.getcwd())  # prints /absolute/path/to/{{cookiecutter.project_slug}}

def remove(filepath):
    print("filepath = %s", filepath)
    if os.path.isfile(filepath):
        os.remove(filepath)
    elif os.path.isdir(filepath):
        shutil.rmtree(filepath)

if "{{ cookiecutter.enable_windows }}".lower() == "n":
    remove(os.path.join("{{cookiecutter.directory_name}}", "windows_configs"))