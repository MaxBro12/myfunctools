from os import path as p
from os import walk


def win_hide_file(name: str):
    from win32con import (
        FILE_ATTRIBUTE_HIDDEN,
    )
    from win32api import (
        SetFileAttributes,
    )

    try:
        SetFileAttributes(name, FILE_ATTRIBUTE_HIDDEN)
        return True
    except FileNotFoundError:
        return False
    else:
        return False


def win_show_file(name: str):
    from win32con import (
        FILE_ATTRIBUTE_NORMAL,
    )
    from win32api import (
        SetFileAttributes,
    )

    try:
        SetFileAttributes(name, FILE_ATTRIBUTE_NORMAL)
        return True
    except FileNotFoundError:
        return False
    else:
        return False


def win_wayfinder(way: str):
    ways = []
    for address, dirs, files in walk(way):
        for name in files:
            address = address.replace(way, '')

            # ? Убираем расширение файлов
            name = name.split('.')[0]

            ful = p.join(address, name)
            temp = []
            while True:
                path, folder = p.split(ful)

                if folder != '':
                    temp.append(folder)
                elif folder == '':
                    break
                if path != '':
                    ful = path
                elif path == '':
                    break
            temp.reverse()
            ways.append(temp)
    return ways
