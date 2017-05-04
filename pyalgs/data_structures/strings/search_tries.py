from abc import ABCMeta, abstractmethod

from pyalgs.data_structures.commons.queue import Queue


class SearchTries(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def put(self, key, value):
        pass

    @abstractmethod
    def get(self, key):
        pass

    @abstractmethod
    def is_empty(self):
        pass

    @abstractmethod
    def size(self):
        pass

    @abstractmethod
    def delete(self, key):
        pass

    @abstractmethod
    def keys(self):
        pass

    @abstractmethod
    def keysWithPrefix(self, prefix):
        pass

    @abstractmethod
    def contains_key(self, key):
        pass

    @staticmethod
    def create():
        return RWaySearchTries()


class Node(object):
    nodes = None
    value = None
    R = 256

    def __init__(self):
        self.nodes = [None] * Node.R


class RWaySearchTries(SearchTries):

    root = None
    N = 0

    def contains_key(self, key):
        x = self._get(self.root, key, 0)
        if x is None:
            return None
        return x.value

    def keysWithPrefix(self, prefix):
        x = self._get(self.root, prefix, 0)
        if x is None:
            return None

        queue = Queue.create()
        self.collect(x, prefix, queue)
        return queue.iterate()

    def keys(self):
        queue = Queue.create()
        self.collect(self.root, '', queue)
        return queue.iterate()

    def collect(self, x, prefix, queue):
        if x is None:
            return

        if x.value is not None:
            queue.enqueue(prefix)
            return

        for r in range(Node.R):
            self.collect(x.nodes[r], prefix + str(chr(r)), queue)

    def is_empty(self):
        return self.N == 0

    def get(self, key):
        x = self._get(self.root, key, 0)
        if x is not None:
            return x.value
        return None

    def _get(self, x, key, d):
        if x is None:
            return None
        if len(key) == d:
            return x

        return self._get(x.nodes[self.char_at(key, d)], key, d + 1)

    def delete(self, key):
        self.root = self._delete(self.root, key, 0)

    def _delete(self, x, key, d):
        if x is None:
            return None

        if len(key) == d:
            if x.value is not None:
                self.N -= 1
            return None

        c = self.char_at(key, d)
        x.nodes[c] = self._delete(x.nodes[c], key, d + 1)
        return x

    def put(self, key, value):
        self.root = self._put(self.root, key, value, 0)

    def _put(self, x, key, value, d):
        if x is None:
            x = Node()
        if len(key) == d:
            if x.value is None:
                self.N += 1
            x.value = value
            return x

        c = self.char_at(key, d)
        x.nodes[c] = self._put(x.nodes[c], key, value, d + 1)
        return x

    def char_at(self, key, d):
        return ord(key[d])

    def size(self):
        return self.N
