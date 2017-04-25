from abc import abstractmethod, ABCMeta


class Queue(object):
    """ Queue interface
    
    """

    __metaclass__ = ABCMeta

    @abstractmethod
    def enqueue(self, item):
        pass

    @abstractmethod
    def dequeue(self):
        pass

    @abstractmethod
    def is_empty(self):
        pass

    @abstractmethod
    def size(self):
        pass

    @staticmethod
    def create():
        return LinkedListQueue()


class Node(object):

    value = None
    nextNode = None

    def __init__(self, value):
        self.value = value


class LinkedListQueue(Queue):

    first = None
    last = None
    N = 0

    def size(self):
        return self.N

    def enqueue(self, item):
        old_last = self.last
        self.last = Node(item)
        if old_last is not None:
            old_last.nextNode = self.last
        if self.first is None:
            self.first = self.last
        self.N += 1

    def is_empty(self):
        return self.N == 0

    def dequeue(self):
        if self.is_empty():
            return None
        old_first = self.first
        self.first = old_first.nextNode
        if old_first == self.last:
            self.last = None
        self.N -= 1
        return old_first.value


class ArrayQueue(Queue):
    head = 0
    tail = 0
    s = []

    def __init__(self, capacity=10):
        self.s = [0] * capacity

    def enqueue(self, item):
        self.s[self.tail] = item
        self.tail += 1
        if self.tail == len(self.s):
            self.resize(len(self.s) * 2)

    def resize(self, new_size):
        tmp = [0] * new_size
        for i in range(self.head, self.tail):
            tmp[i-self.head] = self.s[i]
        self.s = tmp
        self.head = self.head - self.tail
        self.tail = 0

    def size(self):
        return self.tail - self.head

    def is_empty(self):
        return self.size() == 0

    def dequeue(self):
        if self.is_empty():
            return None

        deleted = self.s[self.head]
        self.head -= 1
        if self.size() == len(self.s) / 4:
            self.resize(len(self.s) / 2)
        return deleted
