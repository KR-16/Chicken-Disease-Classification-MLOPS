import os
from pathlib import Path
import logging

logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s]: %(message)s:'
)

project_name = "ChickenDiseaseClassifier"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "research/trials.ipynb"
]

for file_path in list_of_files:
    file_path = Path(file_path)
    file_directory, file_name = os.path.split(file_path)

    if file_directory !="":
        os.makedirs(file_directory, exist_ok=True)
        logging.info(f"Creating Directory: {file_directory} for the file {file_name}")
    if (os.path.exists(file_path)) or (os.path.getsize(file_path) == 0):
        with open(file_path, "w") as f:
            pass
            logging.info("Creating empty file: {file_path}")
    else:
        logging.info(f"{file_name} already exists")