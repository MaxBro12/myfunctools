from os import (
    rename,
    walk,
    path as p,
)


def lin_hide_file(name: str):
    try:
        rename(name, '.' + name)
        return True
    except FileNotFoundError:
        return False
    else:
        return False


def lin_show_file(name: str):
    try:
        rename(name, name.removeprefix('.'))
    except FileNotFoundError:
        return False
    else:
        return False


def lin_wayfinder(way: str):
    ways = []
    for address, dirs, files in walk(way):
        for name in files:
            address = address.replace(way, '')

            # ? Убираем расширение файлов
            name = name.split('.')[0]

            ful = p.join(address, name)
            ful = ful.split('/')
            ways.append(ful)
    return ways
