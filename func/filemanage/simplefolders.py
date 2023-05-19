from os import mkdir, rename
from shutil import rmtree


from ..debug import create_log_file


def create_folder(name: str) -> bool:
    try:
        mkdir(name)
        return True
    except FileExistsError:
        create_log_file(f'Папка с именем {name} уже существует!', 'error')
        return False


def rename_folder(old_name: str, new_name: str) -> bool:
    try:
        rename(old_name, new_name)
        return True
    except FileNotFoundError:
        create_log_file(
            f'Невозможно переименовать папку {old_name} не найдена!', 'error'
        )
        return False


def delete_folder(name: str) -> bool:
    try:
        rmtree(name)
        return True
    except FileNotFoundError:
        create_log_file(
            f'Невозможно удалить папку {name} не найдена!', 'error'
        )
        return False
