from abc import ABCMeta, abstractmethod

from pyalgs.algorithms.commons import util
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
    def keys_with_prefix(self, prefix):
        pass

    @abstractmethod
    def contains_key(self, key):
        pass

    @staticmethod
    def create():
        return RWaySearchTries()


def char_at(key, d):
    return ord(key[d])


class RwayNode(object):
    nodes = None
    value = None
    R = 256

    def __init__(self):
        self.nodes = [None] * RwayNode.R


class RWaySearchTries(SearchTries):

    root = None
    N = 0

    def contains_key(self, key):
        x = self._get(self.root, key, 0)
        if x is None:
            return None
        return x.value

    def keys_with_prefix(self, prefix):
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

        for r in range(RwayNode.R):
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

        return self._get(x.nodes[char_at(key, d)], key, d + 1)

    def delete(self, key):
        self.root = self._delete(self.root, key, 0)

    def _delete(self, x, key, d):
        if x is None:
            return None

        if len(key) == d:
            if x.value is not None:
                self.N -= 1
            return None

        c = char_at(key, d)
        x.nodes[c] = self._delete(x.nodes[c], key, d + 1)
        return x

    def put(self, key, value):
        self.root = self._put(self.root, key, value, 0)

    def _put(self, x, key, value, d):
        if x is None:
            x = RwayNode()
        if len(key) == d:
            if x.value is None:
                self.N += 1
            x.value = value
            return x

        c = char_at(key, d)
        x.nodes[c] = self._put(x.nodes[c], key, value, d + 1)
        return x

    def size(self):
        return self.N


class TSTNode(object):
    value = None
    left = None
    mid = None
    right = None
    key = None

    def __init__(self, c):
        self.key = c


class TernarySearchTries(SearchTries):

    root = None
    N = 0

    def contains_key(self, key):
        x = self._get(self.root, key, 0)
        return x is not None and x.value is not None

    def size(self):
        return self.N

    def keys(self):
        queue = Queue.create()
        self.collect(self.root, '', queue)
        return queue.iterate()

    def collect(self, x, prefix, queue):
        if x is None:
            return
        if x.value is not None:
            queue.enqueue(prefix)
        c = chr(x.key)
        self.collect(x.left, prefix, queue)
        self.collect(x.mid, prefix + str(c), queue)
        self.collect(x.right, prefix, queue)

    def get(self, key):
        x = self._get(self.root, key, 0)
        if x is None:
            return None
        return x.value

    def _get(self, x, key, d):
        if x is None:
            return None
        c = char_at(key, d)
        compared = util.cmp(c, x.key)
        if compared < 0:
            return self._get(x.left, key, d)
        elif compared > 0:
            return self._get(x.right, key, d)
        elif len(key)-1 == d:
            return x
        else:
            return self._get(x.mid, key, d+1)

    def put(self, key, value):
        self.root = self._put(self.root, key, value, 0)

    def _put(self, x, key, value, d):
        c = char_at(key, d)
        if x is None:
            x = TSTNode(c)
        compared = util.cmp(c, x.key)
        if compared < 0:
            x.left = self._put(x.left, key, value, d)
        elif compared > 0:
            x.right = self._put(x.right, key, value, d)
        elif len(key)-1 == d:
            if x.value is None:
                self.N += 1
            x.value = value
        else:
            x.mid = self._put(x.mid, key, value, d+1)

        return x

    def delete(self, key):
        x = self._get(self.root, key, 0)
        if x is not None:
            if x.value is not None:
                self.N -= 1
            x.value = None

    def is_empty(self):
        return self.N == 0

    def keys_with_prefix(self, prefix):
        x = self._get(self.root, prefix, 0)
        if x is None:
            return None
        queue = Queue.create()
        self.collect(x, prefix, queue)
        return queue.iterate()