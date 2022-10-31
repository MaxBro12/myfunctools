from os import (
    mkdir,
    getcwd,
)
from os.path import (
    join,
    exists,
)
from sys import (
    platform,
)


inner_folders = (
    'admin',
    'app',
    'code',
    'source',
)


# ! Шаблоны файлов
gitignore_file = """.vscode\n.idea\n\n__pycache__\n
\n*.bat\npatch.txt\n\ntest.*\n"""
patch_file = '[Заголовок]\n\n[подпись]'
git_to_server_f_bat = ''


def create_gts_bat(way: str):
    msg = f"""cd {way}\ngit add *\n
    git commit -F patch.txt\ngit push origin master"""
    return str(msg)


def create_folder(name: str, way: str = None) -> bool:
    """
    Создает папку по пути way с именем name.
    Если указать путь вместе с названием папки в параметре name,
    переменная way = None.
    Возвращает True или False в зависимости от исхода операции.
    """
    try:
        # ? Проверка создания пустого названия
        if name == '':
            raise ValueError
        # ? Если путь передан в название файла
        if way is None:
            way = name
        else:
            way = join(way, name)

        # ! Создание
        mkdir(way)
        return True
    except FileExistsError:
        print(f'Папка {name} уже существует!')
        return False
    except FileNotFoundError:
        print(f'Ошибка в пути, проверьте путь {way}')
        return False
    except ValueError:
        print(f'Попытка создать папку без названия! "{name}" {way}')


def create_file(
    name: str,
    way: str = None,
    inner_text: str = None
) -> bool:
    """
    Создает файл с названием и расширением, указанным в name,
    по пути way, так же записывает в нутрь текст innet_text.
    Если указать путь вместе с названием папки в параметре name,
    переменная way = None.
    Возвращает True или False в зависимости от исхода операции.
    """
    try:
        # ? Проверяем расширение файла
        if len(name.split('.')) == 1:
            raise ValueError

        # ? Если путь передан в название файла
        if way is None:
            way = name
        else:
            way = join(way, name)

        # ? Защита от перезаписи существующих файлов
        if exists(way):
            raise FileExistsError

        # ! Создание
        with open(way, 'w') as f:
            if inner_text is not None:
                f.write(inner_text)
            f.close()
        return True
    except FileExistsError:
        print(f'Файл {name} уже существует!')
        return False
    except FileNotFoundError:
        print(f'Ошибка в пути, проверьте путь {way}')
        return False
    except ValueError:
        print(f'Попытка создать файл без расширения: {way}')
        return False


def get_proj_name():
    print(
        'Введите путь, где развернуть проект?\n' +
        '(папка проекта создается автоматически следуя его названию)\n' +
        'Если хотите развернуть проект тут:' +
        getcwd()
    )
    project_way = input('Введите Y\n')
    if project_way == 'Y':
        project_way = getcwd()

    project_name = input('Введите название проекта:\n')
    return (project_name, project_way)


def main():
    project_name, project_way = get_proj_name()
    if not create_folder(project_name, project_way):
        print('Не удалось создать проект!')
        if input('Попробовать снова? [Y / n]\n') == 'Y':
            main()
        else:
            return False

    # ! Создаем внутренности проекта
    inner_way = join(project_way, project_name)
    print(inner_way)
    for folder in inner_folders:
        create_folder(folder, inner_way)

    # ! Создаем файлы внутри
    sistem_files = ''
    # * admin
    if platform.startswith('win'):
        create_file(
            'git_push.bat',
            inner_way,
            create_gts_bat(inner_way)
        )

    # * MAIN Folder
    create_file('.gitignore', inner_way, gitignore_file)
    create_file('ReadMe.md', inner_way)
    create_file('patch.txt', inner_way, patch_file)

    return True


if __name__ == '__main__':
    main()
