from pathlib import Path
from typing import List, Union


def read_lines(file_path: Union[str, Path]) -> List[str]:
    file_path_object = Path(file_path)
    with open(file_path_object) as file:
        lines = file.readlines()
    lines = [line.strip() for line in lines]
    return [line for line in lines if line]

