# ! СТРУКТУРЫ ДАННЫХ
# ? Стек - Stack
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


# ? Очередь - Queue
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


# ? Связные Списки - Linked lists
class LinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, head):
        self.head = head
        self.__list = []

    def append(self, item: LinkedListNode):
        self.__list[-1].next = item
        self.__list.append(item)

    @property
    def list(self):
        return self.__list

    @property
    def tail(self):
        return self.__list[-1]

    @property
    def size(self):
        return len(self.__list)

    def __len__(self):
        return len(self.__list)


# ? Циркулярно Связанные Списки - Circularly Linked Lists
class CircListNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircList:
    def __init__(self, head):
        self.head = head
        self.__list = []

    def append(self, item: CircListNode):
        self.__list[-1].next = item
        item.next = self.__list[0]
        self.__list.append(item)

    @property
    def list(self):
        return self.__list

    @property
    def tail(self):
        return self.__list[-1]

    @property
    def size(self):
        return len(self.__list)

    def __len__(self):
        return len(self.__list)


# ? Бинарное дерево - Binary Tree
class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if data < self.data:
            if self.left is None:
                self.left = data
            else:
                self.left.insert(data)
        elif data > self.data:
            if self.right is None:
                self.right = data
            else:
                self.right.insert(data)
        else:
            return False

    def traversePreOrder(self):
        print(self.data, end=' ')
        if self.left:
            self.left.traversePreOrder()
        if self.right:
            self.right.traversePreOrder()

    def traverseInOrder(self):
        if self.left:
            self.left.traverseInOrder()
        print(self.data, end=' ')
        if self.right:
            self.right.traverseInOrder()

    def traversePostOrder(self):
        if self.left:
            self.left.traversePostOrder()
        if self.right:
            self.right.traversePostOrder()
        print(self.data, end=' ')


# ? Хеш Таблица - Hash Table
class HashTable:
    def __init__(self, capacity: int):
        self.__capacity = capacity
        self.__slots = [None] * self.__capacity

    def hashfunction(self, key: int):
        return key % self.__capacity

    def insert(self, key: int, data):
        self.__slots[self.hashfunction(key)] = data

    def remove(self, key: int):
        self.__slots[self.hashfunction(key)] = None

    @property
    def filling_percentage(self):
        return list(map(lambda x: x is None, self.__slots)).count(True) / self.__capacity * 100

    @property
    def capacity(self):
        return self.__capacity

    @property
    def slots(self):
        return self.__slots


# ? Ненаправленные Графы - Undirected Graphs
class Graphs:
    def __init__(self, data, connections: list):
        self.data = data
        self.connections = connections
