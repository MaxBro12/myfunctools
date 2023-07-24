from typing import Any, cast

from toml import load, dump
from ..debug import create_log_file


def read_toml(way: str) -> dict[str, Any]:
    """Считываем файл по пути way формата .toml и возвращаем словарь"""
    return dict(load(way))


def write_to_toml(dictionary, way: str):
    """Записываем словарь dictionary в toml файл по пути way"""
    with open(way, 'w') as toml_file:
        dump(dictionary, toml_file)


def update_dict_to_type(dictionary: dict, type_to):
    """Обновляет словарь до выбранного типа"""
    return cast(type_to, dictionary)
