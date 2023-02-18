from sys import platform


def get_os():
    """Получаем тип ОС"""
    match platform:
        case 'linux' | 'linux2':
            return 'linux'
        case 'win32' | 'cygwin' | 'msys':
            return 'win'
        case 'darwin':
            return 'ios'
        case _:
            return None
