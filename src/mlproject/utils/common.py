import os
from box.exceptions import BoxValueError
import yaml
from mlproject import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Reads yaml file and returns
    Args: 
        path_to_yaml: str
    Returns: 
        ConfigBox: ConfigBox type
    """

    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info("yaml loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml is not in correct format")
    except Exception as e:
        raise e
    

@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """
    Create directories
    Args:
        path_to_directories: list of path of directories
        verbose: flag to show logs
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at {path}")


@ensure_annotations
def save_json(path: Path, data: dict):
    """
    Save json file
    Args:
        path: path to json file
        data: data to be saved as json
    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

    logger.info(f"json file saved at: {path}")


@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """
    Load json file
    Args:
        path: path to json file
    Returns:
        ConfigBox: ConfigBox type
    """
    with open(path) as f:
        content = json.load(f)

    return ConfigBox(content)

@ensure_annotations
def save_bin(data: Any, path: Path):
    """
    Save binary file
    Args:
        data: data to be saved as binary
        path: path to binary file
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"binary file saved at: {path}")


@ensure_annotations
def load_bin(path: Path) -> Any:
    """
    Load binary file
    Args:
        path: path to binary file
    Returns:
        Any: Any type
    """
    return joblib.load(path)

@ensure_annotations
def get_size(path: Path) -> str:
    """
    get size in KB
    Args:
        path: path of the file
    Returns:
        str: size in KB 
    """
    size = os.path.getsize(path)
    return f"{size/1024} KB"
