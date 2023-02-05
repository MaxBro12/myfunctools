from io import StringIO
from pandas import DataFrame, read_csv
from os.path import exists
from code.handlers.decryption import *

class Table:
    def __init__(self):
        self.__base_key = 10
        self.check_data()
        self.__data = None
        self.read_txt()

    def view_current(self) -> str:
        line = int(input('Введите целочисленное значение индекса:\n'))
        key = int(decrypt_lite(str(self.__data.iloc[line]['Ключ']), self.__base_key))
        label = self.__data.iloc[line]['Метка']
        login = decrypt_lite(str(self.__data.iloc[line]['Логин']), key)
        password = decrypt_lite(str(self.__data.iloc[line]['Пароль']), key)
        print(f'Метка: {label}\nЛогин: {login}\nПароль: {password}')
        return key

    def add(self):
        label = input('Введите метку\n')
        key = int(input('Введите строго целочисленное значение (разрешено использовать и отрицательное):\n'))
        login = input('Введите логин:\n')
        password = input('Введите пароль:\n')
        print(f'Верно?\nМетка: {label}\nЛогин: {login}\nПароль: {password}\ny - Да / n - Нет')
        if input() == 'y':
            self.__data.loc[len(self.__data.index)] = (str(label), encrypt_lite(str(key), self.__base_key), encrypt_lite(str(login), key), encrypt_lite(str(password), key))
            self.save_txt()
        else:
            self.add()

    def remove(self):
        delline = int(input('Введите целочисленный индекс строки, которую хотите удалить:\n'))
        self.__data.drop(labels=delline, inplace=True)
        self.save_txt()

    def check_data(self):
        if not exists('data.txt'):
            self.create_csv()

    def create_csv(self):
        df = DataFrame(columns=['Метка', 'Ключ', 'Логин', 'Пароль'])
        file = open('data.txt', 'w')
        file.write(encrypt(df.to_csv(index=False), self.__base_key))
        file.close()

    def save_txt(self):
        text = self.__data.to_csv(index=False)
        text = encrypt(text, self.__base_key)
        file = open('data.txt', 'w')
        file.write(text)
        file.close()

    def read_txt(self):
        file = open('data.txt', 'r')
        text = file.readlines()[0]
        text = decrypt(text, self.__base_key)
        self.__data = read_csv(StringIO(text), sep=',')
        file.close()

    def view(self) -> str:
        print(self.__data.drop(columns=['Ключ', 'Логин', 'Пароль']).head())