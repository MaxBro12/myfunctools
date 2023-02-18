from sys import platform


def get_os():
    """Получаем тип ОС"""
    if platform == "linux" or platform == "linux2":
        return 'linux'
    elif platform == "win32":
        return 'win'
    elif platform == "darwin":
        return 'ios'
    else:
        return None


if __name__ == '__main__':
    print(get_os())
