from os import getenv
from os.path import exists
from dotenv import load_dotenv


def load_env(file_path: str):
    if exists(file_path):
        load_dotenv(file_path)
        return True
    return False


def get_from_env(key: str):
    return getenv(key)

