from abc import ABCMeta, abstractmethod

from pyalgs.algorithms.commons import util
from pyalgs.data_structures.commons.queue import Queue


class HashedSet(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def add(self, key):
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
    def iterate(self):
        pass

    @abstractmethod
    def contains(self, key):
        pass

    @staticmethod
    def create():
        return HashedSetWithSeparateChaining()


class Node(object):
    key = None
    next_node = None

    def __init__(self, key=None):
        self.key = key


class HashedSetWithSeparateChaining(HashedSet):
    M = 97
    id = None
    N = 0

    def __init__(self, m=None):
        if m is None:
            m = 97
        self.M = m
        self.id = [None] * self.M

    def hash(self, key):
        return (hash(key) & 0x7fffffff) % self.M

    def is_empty(self):
        return self.N == 0

    def iterate(self):
        for i in range(self.M):
            x = self.id[i]
            while x is not None:
                key = x.key
                x = x.next_node
                yield key

    def size(self):
        return self.N

    def contains(self, key):
        i = self.hash(key)
        x = self.id[i]
        while x is not None:
            if util.cmp(x.key, key) == 0:
                return True
            x = x.next_node
        return False

    def delete(self, key):
        i = self.hash(key)
        x = self.id[i]
        prev_node = None
        while x is not None:
            if util.cmp(x.key, key) == 0:
                next_node = x.next_node
                self.N -= 1
                if prev_node is not None:
                    prev_node.next_node = next_node
                if self.id[i] == x:
                    self.id[i] = None
                return True
            prev_node = x
            x = x.next_node
        return False

    def add(self, key):
        if key is None:
            raise ValueError('key cannot be None')

        i = self.hash(key)
        x = self.id[i]
        while x is not None:
            if util.cmp(x.key, key) == 0:
                return
            x = x.next_node
        old_first = self.id[i]
        self.id[i] = Node(key)
        self.id[i].next_node = old_first
        self.N += 1


class HashedSetWithLinearProbing(HashedSet):

    M = 97
    id = None
    N = 0

    def __init__(self, m=None):
        if m is None:
            m = 97
        self.M = m
        self.id = [None] * self.M

    def hash(self, key):
        return (hash(key) & 0x7fffffff) % self.M

    def is_empty(self):
        return self.N == 0

    def iterate(self):
        for i in range(self.M):
            x = self.id[i]
            if x is not None:
                yield x.key

    def size(self):
        return self.N

    def contains(self, key):
        i = self.hash(key)
        for j in range(self.M):
            k = (i + j) % self.M
            x = self.id[k]
            if x is None:
                return False
            if util.cmp(key, x.key) == 0:
                return True

    def delete(self, key):
        i = self.hash(key)
        for j in range(self.M):
            k = (i + j) % self.M
            x = self.id[k]
            if x is None:
                return False
            if util.cmp(key, x.key) == 0:
                self.id[k] = None
                self.N -= 1
                if self.N == self.M // 4:
                    self.resize(self.M // 2)
                return True

    def add(self, key):
        i = self.hash(key)
        for j in range(self.M):
            k = (i + j) % self.M
            x = self.id[k]
            if x is None:
                self.id[k] = Node(key)
                self.N += 1
                if self.N == self.M // 2:
                    self.resize(self.M * 2)
                break
            if util.cmp(x.key, key) == 0:
                break

    def resize(self, new_size):
        clone = HashedSetWithLinearProbing(new_size)
        for i in range(self.M):
            x = self.id[i]
            if x is not None:
                clone.add(x.key)
        self.M = clone.M
        self.id = clone.id
