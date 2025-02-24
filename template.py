import os 
from pathlib import Path

project_name = "tsp"

list_of_files = [
    f"{project_name}/__init__.py",
    f"{project_name}/constants/__init__.py",
    f"{project_name}/utils/__init__.py",
    f"{project_name}/exception/__init__.py",
    f"{project_name}/logger/__init__.py",
    f"{project_name}/solver/__init__.py",
    f"{project_name}/solver/tsp_solver.py",
    f"{project_name}/data_model/__init__.py",
    f"{project_name}/data_model/load_data.py",
    f"{project_name}/data_model/create_distance_matrix.py",
    "app.py",
    "requirements.txt",
    "Dockerfile",
    ".dockerignore",
    "demo.py",
    "setup.py",
]

for file in list_of_files:
    filepath = Path(file)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass
    else:
        print(f"File {filepath} already exists.")