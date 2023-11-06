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
