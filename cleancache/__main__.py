from path import pathfinder, remove_dir_tree, split, remove
from sys import argv


def main(path: str, print_files: bool):
    deleted_int = 0
    files = list(map(lambda x: x[0], pathfinder(path)))
    files = list(filter(lambda x: split(x)[-1] == '__pycache__', files))
    if print_files:
        for f in files:
            print(f'> {f}')
    files = list(map(lambda x: remove_dir_tree(x), files))
    print(f'Files deleted: {files.count(True)}')


if __name__ == '__main__':
    try:
        main(argv[-1], True)
    except Exception as err:
        print('ERROR =================\n', err)
