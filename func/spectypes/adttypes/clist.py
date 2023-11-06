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
