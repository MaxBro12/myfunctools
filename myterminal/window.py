import os


class Window():
    def __init__(self):
        self.screen = [' ' * self.size[0] for i in range(self.size[1])]
        self.widgets = ()

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
        """Единоразовая отрисовка в терминал"""
        for i in self.widgets:

    def update_screen(self):
        """Постоянный вывод в терминал"""
        self.prepare_screen()
        while True:
            x, y = self.size


class Widget():
    def __init__(
            self,
            pos_x: int = 0,
            pos_y: int = 0,
            width: int = 5,
            height: int = 1,
            content: str = '',
            style: list = (),
    ):
        self.pos_x = pos_x,
        self.pos_y = pos_y,
        self.width = width,
        self.height = height,
        self.content = content,
        self.style = style,

    @property
    def show(self):
        return f'{self.style[0]} {self.content[:self.width]} {self.style[1]}'
