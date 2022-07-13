from types import NoneType


class UserInp:
    def __init__(self):
        self.progrun = False
        self.commands = {
            'help': self.help,
            'stop': self.stop,
            'hello': self.hello
        }

    def run(self):
        self.progrun = True
        
        while self.progrun:
            self.user_input()
    
    def user_input(self): # TODO: Доработать обработку исключений!
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
            except TypeError:
                print('Wrong command!')
                self.user_input()
        else:
            print(f'Unknown command: "{com}"')

    def help(self, adt = None):
        if isinstance(adt, NoneType):
            print('List of all commands:')
            for command in self.commands:
                print(f'\t{command} - {self.commands[command].__doc__}')
        else:
            try:
                adt = str(adt[0])
                if adt in self.commands:
                    print(f'info about {adt}:\n\t{self.commands[adt].__doc__}')
            except TypeError:
                print(f'Unknown command {adt}, use "help" command')
                self.user_input()

    def stop(self):
        '''Stopping user input'''
        self.progrun = False

    # * Твои дополнительные функции или методы
    def hello(self):
        '''Printing hello \o/'''
        print('Hello, world!')
