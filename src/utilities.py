from pathlib import Path
from typing import Union

import yaml
from yaml import Loader



def read_yaml(file: Union[str, Path], key: str = None) -> dict:
    with open(file, "r") as fp:
        params = yaml.load(fp, Loader)
    return params[key] if key else params


def dump_yaml(obj: dict, file_path: Union[str, Path], key: str = None) -> Path:
    with open(file_path, "w+") as file:
        yaml.dump(obj, file)
    return Path(file_path)