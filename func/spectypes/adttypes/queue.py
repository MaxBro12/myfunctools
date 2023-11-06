class Queue:
    """Реализация очереди"""
    def __init__(self):
        self.__queue = []

    def enqueue(self, item):
        self.__queue.append(item)

    def dequeue(self):
        if len(self.__queue) == 0:
            return None
        return self.queue.pop(0)

    @property
    def queue(self):
        return self.__queue

    @property
    def size(self):
        return len(self.__queue)

    def __len__(self):
        return len(self.__queue)


class QueueLimited:
    """Класс очередь но с ограниченным кол-вом места"""
    def __init__(self, max_size: int = 5):
        self.__queue = []
        self.__max_size = int(max_size)

    def enqueue(self, item):
        self.__queue.append(item)
        if len(self.__queue) > self.__max_size:
            self.__queue.__delitem__(0)

    def dequeue(self):
        if len(self.__queue) == 0:
            return None
        return self.queue.pop(0)

    @property
    def queue(self):
        return self.__queue

    @property
    def size(self):
        return len(self.__queue)

    @property
    def sizemax(self):
        return self.__max_size

    def __len__(self):
        return len(self.__queue)


# ? Очередь с приоритетом - Priority Queue
class PQueueNode:
    def __init__(self, data, priority: int):
        self.data = data
        self.priority = priority


class PQueue:
    def __init__(self):
        self.__queue = []

    def enqueue(self, item, priority: int):
        item = PQueueNode(item, priority)
        self.__queue.append(item)
        self.__queue.sort(key=lambda x: x.priority, reverse=True)

    def dequeue(self):
        if len(self.__queue) == 0:
            return None
        return self.queue.pop(0)

    @property
    def queue(self):
        return self.__queue

    @property
    def size(self):
        return len(self.__queue)

    def __len__(self):
        return len(self.__queue)
