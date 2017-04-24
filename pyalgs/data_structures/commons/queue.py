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


class Node(object):

    value = None
    nextNode = None

    def Node(self, value):
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
