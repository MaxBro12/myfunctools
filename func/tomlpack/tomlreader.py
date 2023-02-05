from toml import load, dump


def read(way: str) -> dict:
    """Считываем файл по пути way формата .toml и возвращаем словарь"""
    return load(way)


def write(dictionary: dict, way: str):
    """Записываем словарь dictionary в toml файл по пути way.\nway обязана указывать на сам файл формата .toml"""
    with open(way, 'w') as toml_file:
        dump(dictionary, toml_file)
