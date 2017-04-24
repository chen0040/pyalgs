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
    def isEmpty(self):
        pass

    @abstractmethod
    def size(self):
        pass


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

    def pop(self):
        if self.isEmpty():
            return None
        old_first = self.first
        if old_first.nextNode is None:
            self.first = None
        self.first = old_first.nextNode
        self.N -= 1
        return old_first

    def isEmpty(self):
        return self.N == 0

    def size(self):
        return self.N
