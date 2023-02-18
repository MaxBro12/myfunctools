from toml import load, dump
from .exceptions import ConfigException


def read(way: str) -> dict:
    """Считываем файл по пути way формата .toml и возвращаем словарь"""
    try:
        return load(way)
    except Exception:
        return ConfigException


def write(dictionary: dict, way: str):
    """Записываем словарь dictionary в toml файл по пути way.\nway обязана указывать на сам файл формата .toml"""
    try:
        with open(way, 'w') as toml_file:
            dump(dictionary, toml_file)
    except Exception:
        return ConfigException
