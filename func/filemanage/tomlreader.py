from typing import Any

from toml import load, dump
from ..debug import create_log_file


def read(way: str) -> dict[str, Any]:
    """Считываем файл по пути way формата .toml и возвращаем словарь"""
    return dict(load(way))


def write(dictionary, way: str):
    """Записываем словарь dictionary в toml файл по пути way"""
    with open(way, 'w') as toml_file:
        dump(dictionary, toml_file)
