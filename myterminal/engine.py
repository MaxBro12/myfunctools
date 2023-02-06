from .lang import (
    ru,
    en,
)
from .excep import (
    KillException,
)
from .eng_settings import (
    confirmation,
    rejection,
)


emp_conf = {
    'debug': True,
    'lang': 'ru',
}


class UserInp:
    def __init__(self, config: dict = emp_conf, args: list = None):
        # ? Загружаем конфиг файл в формате словаря
        self.config = config

        # ? Загружаем языковую базу
        self.lang = None
        self.change_lang()

        # ? Настройки запуска
        self.progrun = False

        # ? Список команд
        self.commands = {
            'admin': self.admin,
            'help': self.help,
            'stop': self.stop,
            'config': self.config_manage,
            'hello': self.hello,
        }

        # ! Запуск в режиме 1 команды
        if args is not None:
            self.run_only_arg(args)

    # ! Основные команды
    def run(self):
        self.progrun = True

        # ? Вывод приветстренного сообщения
        self.start_message()

        # ? Главный цикл программы
        while self.progrun:
            self.user_input()

    def run_only_arg(self, args: list):
        """Запуск определенного действия без запуска всего интерфейса"""
        word = args[0]
        if word in self.commands:
            word = self.commands[word]
            try:
                if len(args) > 1:
                    addition = args[1::]
                    return word(addition)
                else:
                    return word()
            except TypeError as error:
                print(self.lang['incorectm'])
                if self.config['debug']:
                    print(error)
        else:
            print(f'{self.lang["uncom"]}"{word}"')

    def user_input(self):
        """
        Метод пользовательского ввода.
        Запускает набранную команду из списка команд.
        """
        word = str(input(': ')).split()
        if word == []:
            return self.user_input()
        com = word[0]
        if com in self.commands:
            command = self.commands[com]
            try:
                if len(word) > 1:
                    addition = word[1::]
                    return command(addition)
                else:
                    return command()
            except TypeError as error:
                print(self.lang['incorectm'])
                if self.config['debug']:
                    print(error)
                return self.user_input()
        else:
            print(f'{self.lang["uncom"]}"{com}"')

    def help(self, adt=None):
        """Вывод сообщения о помощи"""
        def printer(com: str):
            print(f'[{com}] -> {self.lang[com]}')
        if adt is None:
            self.help_message()
        elif adt[0] in ('l', 'list'):
            for com in self.commands:
                if com == 'admin':
                    continue
                printer(com)
        else:
            for com in adt:
                if com in self.commands.values():
                    printer(com)

    def stop(self):
        """Останавливает пользовательский ввод"""
        self.progrun = False

    def admin(self, args: list):
        """Специальные команды для администратора"""
        match args[0]:
            case 'kill':
                raise KillException
            case 'update':
                self.update_conf()

    def update_conf(self):
        "Обновление корфигурации интерфейса и сохранение его настроек"
        # ! Сюда подключить метод сохранения конфигурации в файл
        # ! Например использовать мой tomlpack
        # ! Connect the method for saving the configuration to a file here
        # ! For example use my tomlpack
        self.change_lang()
        print(self.lang['updateconf'])

    def change_lang(self):
        """Перезагружает языковой пакет"""
        match self.config['lang']:
            case 'ru':
                self.lang = ru
            case 'en':
                self.lang = en
            case _:
                self.lang = ru

    def config_manage(self):
        """Режим изменения настроек"""
        print(self.lang['confs'])
        for index, i in enumerate(self.config):
            print(
                f': [{index}] {i}{" " * (10 - len(str(i)))}-> {self.config[i]}'
            )
        while True:
            param = input(self.lang['confselect'])
            if param == '':
                break
            else:
                if param in self.config.values():
                    new_val = input(self.lang['confnew'])
                    self.config[param] = new_val
                else:
                    print(self.lang['confnotfound'])
                    continue
        self.update_conf()

    # ? Сообщения помощи и старта
    def start_message(self):
        """Вывод стартового сообщения"""
        print(self.lang['startm'])

    def help_message(self):
        """Вывод сообщения помощи"""
        print(
            self.lang['helpm']
        )

    # ! === Пользовательские методы === Custom Methods ========================
    '''
    Для стабильной работы команда (она же является методом класса) должна:
    1) Иметь документацию. Именно она выписывается как описание
    с использованием команды help
    2) print - команды должны что-то выводить
    3) args - аргументы в функции передаются одним списком
    Пример:
    Команда - help hello в виде интерпретатора выглядит
    как метод help с единственным аргументом ['hello'] являющимся списком
    Разделяется все пробелом:
    help hello stop = self.help(self, ['hello', 'stop'])
    Так же все что передается в аргумент является строкой!
    4) Все команды должны быть в словаре self.commands:
    ключ - слово как обращаться к функции
    значение - метод
    5) Названия команд не должны иметь в названии:
    - пробел
    - специальные символы, не все консоли могут их поддерживать
    Рекомендуется для ввода использовать стандартные латинские символа,
    вывод же может быть любым языком.
    '''

    def hello(self, args: list = ['']):
        """Выводит 'Hello, world!'"""
        print(f'Hello, world! {args[0]}')
