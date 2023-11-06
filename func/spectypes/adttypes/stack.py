class Stack:
    """Реализация Stack"""
    def __init__(self):
        self.__stack = []

    def push(self, item):
        self.__stack.append(item)

    def pop(self):
        if len(self.__stack) == 0:
            return None
        return self.__stack.pop()

    @property
    def stack(self):
        return self.__stack

    @property
    def size(self):
        return len(self.__stack)

    def __len__(self):
        return len(self.__stack)


class StackLimited:
    """Реализация Stack, но с ограниченым кол-вом места"""
    def __init__(self, max_size: int = 5):
        self.__stack = []
        self.__max_size = int(max_size)

    def push(self, item):
        self.__stack.append(item)
        if self.size > self.__max_size:
            self.stack.__delitem__(0)

    def pop(self):
        if len(self.__stack) == 0:
            return None
        return self.__stack.pop()

    @property
    def stack(self):
        return self.__stack

    @property
    def size(self):
        return len(self.__stack)

    @property
    def sizemax(self):
        return self.__max_size

    def __len__(self):
        return len(self.__stack)
