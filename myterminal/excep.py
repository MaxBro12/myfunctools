class KillException(Exception):
    def __init__(self):
        self.txt = 'Пользователь вызвал исключение'
        super().__init__(self.txt)
