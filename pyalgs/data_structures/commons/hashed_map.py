from abc import ABCMeta, abstractmethod

from pyalgs.algorithms.commons import util
from pyalgs.data_structures.commons.queue import Queue


class HashedMap(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def put(self, key, value):
        pass

    @abstractmethod
    def get(self, key):
        pass

    @abstractmethod
    def delete(self, key):
        pass

    @abstractmethod
    def size(self):
        pass

    @abstractmethod
    def is_empty(self):
        pass

    @abstractmethod
    def keys(self):
        pass

    @abstractmethod
    def contains_key(self, key):
        pass

    @staticmethod
    def create():
        return HashedMapWithSeparateChaining()


class Node(object):
    key = None
    value = None
    next_node = None

    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value


class HashedMapWithSeparateChaining(HashedMap):
    M = 97
    id = None
    N = 0

    def __init__(self):
        self.id = [Node()] * self.M

    def hash(self, key):
        return (hash(key) & 0x7fffffff) % self.M

    def is_empty(self):
        return self.N == 0

    def contains_key(self, key):
        return self.get(key) is not None

    def keys(self):
        queue = Queue.create()
        for i in range(self.M):
            self.collect_keys(i, queue)
        return queue.iterate()

    def collect_keys(self, i, queue):
        x = self.id[i]
        while x is not None:
            queue.enqueue(x.key)
            x = x.next_node

    def size(self):
        return self.N

    def get(self, key):
        i = self.hash(key)
        x = self.id[i]
        while x is not None:
            if util.cmp(x.key, key) == 0:
                return x.value
            x = x.next_node
        return None

    def delete(self, key):
        i = self.hash(key)
        x = self.id[i]
        prev_node = None
        while x is not None:
            if util.cmp(x.key, key) == 0:
                value = x.value
                next_node = x.next_node
                self.N -= 1
                if prev_node is not None:
                    prev_node.next_node = next_node
                if self.id[i] == x:
                    self.id[i] = None
                return value
            prev_node = x
            x = x.next_node
        return None

    def put(self, key, value):
        i = self.hash(key)
        x = self.id[i]
        while x is not None:
            if util.cmp(x.key, key) == 0:
                x.value = value
                return
            x = x.next_node
        old_first = self.id[i]
        self.id[i] = Node(key, value)
        self.id[i].next_node = old_first
        self.N += 1
