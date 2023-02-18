from .lang import (
    ru,
    en,
)
from .exceptions import (
    KillException,
)
from .eng_settings import (
    confirmation,
    rejection,
    config_loc,
    conf_separator,
)
from .tomlreader import (
    read,
    write,
)


emp_conf = {
    'MAIN': {
        'debug': True,
        'lang': 'ru',
    }
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

        # !!! ЭТОТ КОД СКОПИРОВАТЬ В ОБОЛОЧКУ КЛАССА !!!
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
                if self.config['MAIN']['debug']:
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
                if self.config['MAIN']['debug']:
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

    def update_conf(self, config_log: str = config_loc):
        "Обновление корфигурации интерфейса и сохранение его настроек"
        # ! Сюда подключить метод сохранения конфигурации в файл
        write(self.config, config_loc)
        self.change_lang()
        print(self.lang['updateconf'])

    def change_lang(self):
        """Перезагружает языковой пакет"""
        match self.config['MAIN']['lang']:
            case 'ru':
                self.lang = ru
            case 'en':
                self.lang = en
            case _:
                self.lang = ru

    def config_manage(self):
        """Режим изменения настроек"""
        # ? Метод вывода конфига
        def print_conf():
            print(conf_separator)
            for i in self.config:
                if type(self.config[i]) == dict:
                    print(i, ' ┐')
                    for j in self.config[i]:
                        print(
                            f'{" " * len(self.config[i])}' +
                            f'└ {j}{" " * (10 - len(str(j)))}-> ' +
                            f'{self.config[i][j]}'
                        )
                else:
                    print(
                        f'{i}{" " * (10 - len(str(i)))}-> {self.config[i]}'
                    )
            print(conf_separator)

        # ? Общение с пользователем
        print(self.lang['confs'])
        print_conf()
        while True:
            param = input(self.lang['confselect'])
            if param == '':
                break
            else:
                param = param.split(' ')
                if len(param) > 1:
                    if param[0] in self.config.keys():
                        if param[1] in self.config[param[0]].keys():
                            new_val = input(self.lang['confnew'])
                            self.config[param[0]][param[1]] = new_val
                            print_conf()
                elif param[0] in self.config.keys():
                    new_val = input(self.lang['confnew'])
                    self.config[param[0]] = new_val
                    print_conf()
                else:
                    print(self.lang['confnotfound'])
                    continue

        # ? Обновляем конфигурацию
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
    """
    Для стабильной работы:
    1) Создать отдельный модуль "обертку" класса.
    2) Подключить метод сохранения конфигурационных файлов.
    3) В новом классе создать словарь с командами и объединить с self.commands

    Для создания своих методов:
    1) Добавить метод в словарь команд.
    2) Прописать в пакет языка документацию метода.
    3) Метод принимает только список из переданных в него аргуметов.
    """

    def hello(self, args: list = ['']):
        """Выводит 'Hello, world!'"""
        print(f'Hello, world! {args[0]}')
