import os
from box.exceptions import BoxValueError
import yaml
from ChickenDiseaseClassifier import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64

"""
Reading the YAML File
"""

@ensure_annotations
def readYaml(path_to_yaml: Path) -> ConfigBox:
    """
    read yaml file and returns

    Args:
    path_to_yaml (str): path like input

    Raises:
    ValueError: if yaml file is empty
    e: empty file

    Returns:
    ConfigBox: ConfigBox type
    """

    try:
        with open(path_to_yaml) as yamlFile:
            content = yaml.safe_load(yamlFile)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("YAML file is empty")
    except Exception as e:
        raise e


@ensure_annotations
def createDirectories(path_to_directories: list, verbose = True):
    """
    create list of directories

    Args:
    path_to_directories (list): list of path of directories
    ignore_log(bool, optional): ignore if multiple dirs is to be created. Default to False
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created Directory at {path}")

@ensure_annotations
def saveJson(path: Path, data: dict):
    """
    Save JSON data

    Args:
    path(Path): path to JSON file
    data(dict): data to be saved in JSON file
    """
    with open(path,"w") as f:
        json.dump(data, f, indent=4)
    
    logger.info(f"JSON file saved at {path}")

@ensure_annotations
def loadJson(path: Path) -> ConfigBox:
    """
    Load JSON files data
    Args:
    path (Path): path to JSON file

    Returns:
    ConfigBox: data as class attributes instead of dict
    """
    with open(path) as f:
        content = json.load(f)

    logger.info(f"JSON file loaded successfully from: {path}")
    return ConfigBox(content)

@ensure_annotations
def saveBin(data: Any, path: Path):
    """
    Save Binary file
    Args:
    data(Any): data to be saved as binary
    path(Path): path to binary file
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"Binary File saved at {path}")

@ensure_annotations
def loadBin(path: Path) -> Any:
    """
    Load Binary Data

    Args:
    path(Path): path to binary file

    Returns:
    Any: Object stored in the file
    """
    data = joblib.load(path)
    logger.info(f"Binary file loaded from: {path}")
    return data

@ensure_annotations
def getSize(path: Path) -> str:
    """
    Get Size in KB

    Args:
    path(Path): path of the file

    Returns:
    str: size in KB
    """
    sizeKB = round(os.path.getsize(path)/1024)
    return f"~{sizeKB} KB"

def decodeImage(imgString, fileName):
    imgData = base64.b64decode(imgString)
    with open(fileName, "wb") as f:
        f.write(imgData)
        f.close()

def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath, "rb") as f:
        return base64.b64encode(f.read())