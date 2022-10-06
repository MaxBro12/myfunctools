from types import NoneType


class UserInp:
    def __init__(self):
        self.bug_rep = True
        self.progrun = False
        self.commands = {
            'help': self.help,
            'stop': self.stop,
            'hello': self.hello
        }

    def run(self):
        self.progrun = True

        # ! Вывод приветстренного сообщения
        self.start_message()

        # ! Главный цикл программы
        while self.progrun:
            self.user_input()

    def start_message(self):
        print('Use "help" command for more info')

    def user_input(self):
        '''
        Метод пользовательского ввода.
        Запускает набранную команду из списка команд.
        '''
        word = str(input(': ')).split()
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
                print('Wrong command!')
                if self.bug_rep:
                    print(error)
                self.user_input()
        else:
            print(f'Unknown command: "{com}"')

    def help(self, adt=None):
        '''Помощь!'''
        if isinstance(adt, NoneType):
            print('List of all commands:')
            for command in self.commands:
                print(f'\t{command} - {self.commands[command].__doc__}')
        else:
            for com in adt:
                try:
                    adt = str(com)
                    if adt in self.commands:
                        print(f'Docs {adt}:\n\t{self.commands[adt].__doc__}')
                    else:
                        print(f'Unknown command {adt}, use "help" command')
                except Exception as error:
                    print(error)
                    self.user_input()

    def stop(self):
        '''Stopping user input'''
        self.progrun = False

    # ? =============== Функции =================
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
    '''

    def hello(self, args):
        '''Printing hello \\o/'''
        print(f'Hello, world! {args[0]}')
