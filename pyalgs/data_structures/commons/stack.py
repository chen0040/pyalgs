from abc import ABCMeta, abstractmethod


class StackNode(object):
    item = None
    nextNode = None

    def __init__(self, item):
        self.item = item


class Stack(object):
    """ Stack interface which provides the API for stack data structure
    """

    __metaclass__ = ABCMeta

    @abstractmethod
    def push(self, item):
        pass

    @abstractmethod
    def pop(self):
        pass

    @abstractmethod
    def is_empty(self):
        pass

    @abstractmethod
    def size(self):
        pass

    @abstractmethod
    def iterate(self):
        pass

    @staticmethod
    def create():
        return LinkedListStack()


class LinkedListStack(Stack):
    """ Linked list implementation of stack
    """
    first = None
    N = 0

    def push(self, item):
        node = StackNode(item)
        old_first = self.first
        node.nextNode = old_first
        self.first = node
        self.N += 1

    def pop(self):
        if self.is_empty():
            return None
        old_first = self.first
        if old_first.nextNode is None:
            self.first = None
        self.first = old_first.nextNode
        self.N -= 1
        return old_first.item

    def is_empty(self):
        return self.N == 0

    def size(self):
        return self.N

    def iterate(self):
        x = self.first
        while x is not None:
            value = x.item
            x = x.nextNode
            yield value


class ArrayStack(Stack):
    """ Array implementation of stack
    """

    def __init__(self, capacity=None):
        if capacity is None:
            capacity = 10
        self.s = [0] * capacity
        self.N = 0

    def push(self, item):
        self.s[self.N] = item
        self.N += 1
        if self.N == len(self.s):
            self.resize(len(self.s) * 2)

    def resize(self, new_size):
        tmp = [0] * new_size
        for i in range(min(new_size, len(self.s))):
            tmp[i] = self.s[i]
        self.s = tmp

    def pop(self):
        value = self.s[self.N-1]
        self.N -= 1
        if self.N == len(self.s) // 4:
            self.resize(len(self.s) // 2)
        return value

    def is_empty(self):
        return self.N == 0

    def size(self):
        return self.N

    def iterate(self):
        if self.is_empty():
            return
        for i in reversed(range(self.N)):
            yield self.s[i]
