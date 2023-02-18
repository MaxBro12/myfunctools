def create_gitp(way: str, cmd: str = ''):
    msg = f"""cd {way}\ngit add *\ngit commit -F patch.txt\ngit push origin master"""
    return msg


def create_exe(way: str, cmd: str = ''):
    msg = f"""cd {way}\npyinstaller "{way}" --onefile"""
    return msg
