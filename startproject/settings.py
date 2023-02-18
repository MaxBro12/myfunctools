
# ! Директории проекта
dirs = (
    'app',
    'code',
    'admin',
)

files_all = (
    'README.md',
    '.gitignore',
    'code/requirements.txt',
    'code/__main__.py',
    'code/__init__.py',
    'admin/path.txt'
)

files_lin = (
    'admin/git_push.bat',
    'admin/py_to_exe.bat',
)

files_win = (
    'admin/git_push.bash',
    'admin/py_to_exe.bash',
)

# ! Файлы проекта
gitignore = """__pycache__\n*.bat\n*.bash\npatch.txt\n\n.vscode\n.idea\n\ntest\ntest.*\n*.exe\n"""
patch_file = '[Title]\n\n[Description]'
main_file = "\nif __name__ == '__main__':\n\tpass"

# ? Заглушки
bash = "#!/bin/bash\n\n"
zsh = "#!/bin/zsh"

# ? Да / нет
agreement = ['Y', 'y', 'Д', 'д']
disagree = ['n', 'н']
