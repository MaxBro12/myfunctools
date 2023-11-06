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
