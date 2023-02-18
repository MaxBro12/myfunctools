from sys import argv
from os.path import exists, join
from os import listdir, mkdir, system

from myos import get_os
from filecreators import create_file
from textgen import create_gitp, create_exe
from settings import (
    agreement,
    disagree,

    dirs,
    files_all,
    files_lin,
    files_win,

    gitignore,
    patch_file,
    main_file,
)


def get_where() -> str:
    where = ''
    while True:
        where = input('Полный путь директории проекта:\n')
        if not exists(where):
            if input(f'Создать проект в\n{where}\n') in agreement:
                break
        else:
            if len(listdir(where)) != 0:
                if input('Директория занята! Продолжить? ') in agreement:
                    break
            break
    return where


def main(args: list = None):
    # ! Получаем директорию расположения проета
    where = ''
    if args is None:
        where = get_where()
    else:
        if not exists(args[0]):
            print(f'Директория {args[0]} не существует!')
            if input('Создать её? ') in agreement:
                where = args[0]
            else:
                where = get_where()
        else:
            where = args[0]

    # ! Создание проекта
    # ? Получаем ос
    files = files_all
    c_os = get_os()
    if c_os == 'w':
        files += files_win
    elif c_os == 'l':
        files += files_lin

    # ? Создаем директорию
    if not exists(where):
        mkdir(where)
    for i in dirs:
        mkdir(join(where, i))

    # ? Создаем файлы
    for i in files:
        create_file(join(where, i), inner_text='')
        match i:
            case '.gitignore':
                with open(join(where, i), 'w') as f:
                    f.write(gitignore)
            case 'admin/path.txt':
                with open(join(where, i), 'w') as f:
                    f.write(patch_file)
            case 'code/__main__.py':
                with open(join(where, i), 'w') as f:
                    f.write(main_file)
            case 'admin/git_push.bat' | 'admin/git_push.bash':
                with open(join(where, i), 'w') as f:
                    f.write(create_gitp(where))
            case 'admin/py_to_exe.bat' | 'admin/py_to_exe.bash':
                with open(join(where, i), 'w') as f:
                    f.write(create_exe(where))

    # ! Запуск гита
    system(f'git init {where}')


if __name__ == '__main__':
    try:
        if len(argv) != 1:
            argv = argv[1:]
            main(argv)
        main()
    except Exception as error:
        print(error)
