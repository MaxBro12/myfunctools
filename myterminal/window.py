import os


class Window():
    def __init__(self):
        self.screen = [['*' for j in range(self.size[0])] for i in range(self.size[1])]

    @property
    def size(self):
        """Получаем размер терминала"""
        x, y = os.get_terminal_size()
        return x, y

    def prepare_screen(self):
        """Подготовка экрана. Возможно потом удалю этот метод"""
        # ? Чистим экран
        os.system('cls||clear')

    def draw(self):


    def update_screen(self):
        """Вывод в терминал"""
        self.prepare_screen()
        while True:
            x, y = self.size
            for i in range(x):
                for j in range(y):
                    
