import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

Project_name = "CNN_Classifier"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/ __init__.py",
    f"src/components/ __init__.py",
    f"src/utils/ __init__.py",
    f"src/config/ __init__.py",
    f"src/config/configuration.py",
    f"src/pipeline/ __init__.py",
    f"src/entity/ __init__.py",
    f"src/constants/ __init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html"
    
]

for file_path in list_of_files:
    file_path = Path(file_path)
    filedir, filename = os.path.split(file_path)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating dir: {filedir} for the file: {filename}")

    elif (not os.path.exists(file_path)) or (os.path.getsize(file_path)) == 0:
        with open(file_path, "w") as file:
            pass
            logging.info(f"Creating empty file {file_path}")

    else:
        logging.info(f"{filename} already exists")