from sys import platform


def get_os():
    """Получаем тип ОС"""
    if platform == "linux" or platform == "linux2":
        return 'l'
    elif platform == "win32":
        return 'w'
    elif platform == "darwin":
        return 'ios'
    else:
        return None
