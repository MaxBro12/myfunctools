from os import listdir, getcwd, remove, rmdir
from os.path import join, exists, isfile, split, abspath
from typing import Tuple, List
import sys


def pjoin(*args: str) -> str:
    """Соединяет аргументы в путь до файла или папки"""
    return join(*args)


def pjoin_r(*args: str) -> str:
    """Соединяет аргументы в путь до файла или папки"""
    return resource_path(join(*args))


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = abspath(".")
    return join(base_path, relative_path)


def is_file_fast(way_to_file: str) -> bool:
    """Быстрый ответ на вопрос файл это или папка.
    Узнает файл если у него есть разрешение.
    Не работает с файлами без разрешений"""
    try:
        return True if len(split(way_to_file)[1].split('.')) > 1 else False
    except FileNotFoundError:
        # create_log_file(f'File {file_name} not found')
        return False


def is_file_slow(way_to_file: str) -> bool:
    """Узнает файл это или папка путем метода os.path.isfile()"""
    try:
        return True if isfile(way_to_file) else False
    except FileNotFoundError:
        # create_log_file(f'File {way_to_file} not found')
        return False


def wayfinder(way: str) -> bool:
    """Проверяет существование пути way"""
    return True if exists(way) else False


def listdir_path(where: str) -> list:
    """Возвращает список файлов по пути where с добавлением пути"""
    return list(map(lambda x: pjoin(where, x), listdir(where)))


def pathfinder(
        where: str, ignore: tuple | list = ()
) -> List[Tuple[str, bool]] | None:
    """Составляет список файлов и папок найденый всех по пути where.
    Отдельно модуль игнорирует файлы в списке ignore."""
    try:
        if wayfinder(where):
            list_raw = listdir_path(where)
            list_of_files = []
            for i in list_raw:
                if split(i)[1] not in ignore:
                    if not is_file_slow(i):
                        list_raw += listdir_path(i)
                        list_of_files.append((i, False))
                    else:
                        list_of_files.append((i, True))
            return list_of_files
    except Exception as Err:
        # create_log_file(Err, 'error')
        print(Err)


def remove_dir_tree(way_to_folder_name: str) -> bool:
    """Удаляет всю структуру из файлов и папок после пути"""
    try:
        files = pathfinder(way_to_folder_name)
        if files is not None:
            files = files[::-1]
            for i in files:
                if i[1]:
                    remove(i[0])
                else:
                    rmdir(i[0])
            rmdir(way_to_folder_name)
            return True
        return False
    except Exception as Err:
        # create_log_file(Err, 'error')
        print(Err)
        return False
