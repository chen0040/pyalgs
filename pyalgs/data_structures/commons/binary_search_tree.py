from abc import ABCMeta
from pyalgs.algorithms.commons.util import cmp
from pyalgs.data_structures.commons.queue import Queue


class Node(object):
    key = None
    value = None

    left = None
    right = None

    count = 0
    red = 1

    def __init__(self, key, value, red=None):
        self.key = key
        self.value = value
        self.count = 1

        if red is not None:
            self.red = red
        else:
            self.red = 0


def _count(x):
    if x is None:
        return 0
    return x.count


class BinarySearchTree(object):
    __metaclass__ = ABCMeta

    root = None

    def put(self, key, value):
        self.root = self._put(self.root, key, value)

    def _put(self, x, key, value):
        if x is None:
            return Node(key, value)

        compared = cmp(key, x.key)

        if compared < 0:
            x.left = self._put(x.left, key, value)
        elif compared > 0:
            x.right = self._put(x.right, key, value)
        else:
            x.value = value

        x.count = 1 + _count(x.left) + _count(x.right)

        return x

    def get(self, key):
        x = self._get(self.root, key)
        if x is None:
            return None
        return x.value

    def _get(self, x, key):
        if x is None:
            return None
        compared = cmp(key, x.key)
        if compared < 0:
            return self._get(x.left, key)
        elif compared > 0:
            return self._get(x.right, key)
        else:
            return x

    def size(self):
        return _count(self.root)

    def is_empty(self):
        return self.root is None

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, x, key):
        if x is None:
            return None

        compared = cmp(key, x.key)
        if compared < 0:
            x.left = self._delete(x.left, key)
        elif compared > 0:
            x.right = self._delete(x.right, key)
        else:
            if x.left is None:
                return x.right
            elif x.right is None:
                return x.left
            else:
                m = self.min(x.right)
                m.right = self.del_min(x.right)
                m.left = x.left

                x = m

        x.count = 1 + _count(x.left) + _count(x.right)
        return x

    def min(self, x):
        if x.left is None:
            return x
        return self.min(x.left)

    def del_min(self, x):
        if x.left is None:
            return x.right
        x.left = self.del_min(x.left)
        return x

    def contains_key(self, x):
        return self.get(x) is not None

    def keys(self):
        queue = Queue.create()
        self.collect_keys(self.root, queue)
        return queue.iterate()

    def collect_keys(self, x, queue):
        if x is None:
            return

        self.collect_keys(x.left, queue)
        queue.enqueue(x.key)
        self.collect_keys(x.right, queue)

    @staticmethod
    def create():
        return BinarySearchTree()

    @staticmethod
    def create_red_black_tree():
        return RedBlackTree()


class RedBlackTree(BinarySearchTree):
    def put(self, key, value):
        self.root = self._put2(self.root, key, value)

    def _put2(self, x, key, value):
        if x is None:
            return Node(key, value, 1)
        compared = cmp(key, x.key)
        if compared < 0:
            x.left = self._put2(x.left, key, value)
        elif compared > 0:
            x.right = self._put2(x.right, key, value)
        else:
            x.value = value

        if self.is_red(x.right) and not self.is_red(x.left):
            x = self.rotate_left(x)
        if self.is_red(x.left) and self.is_red(x.left.left):
            x = self.rotate_right(x)
        if self.is_red(x.left) and self.is_red(x.right):
            x = self.flip_colors(x)

        x.count = 1 + _count(x.left) + _count(x.right)
        return x

    def _delete(self, x, key):
        if x is None:
            return None

        compared = cmp(key, x.key)
        if compared < 0:
            x.left = self._delete(x.left, key)
        elif compared > 0:
            x.right = self._delete(x.right, key)
        else:
            if x.left is None:
                return x.right
            elif x.right is None:
                return x.left
            else:
                m = self.min(x.right)
                m.right = self.del_min(x.right)
                m.left = x.left

                x = m

        if self.is_red(x.right) and not self.is_red(x.left):
            x = self.rotate_left(x)
        if self.is_red(x.left) and self.is_red(x.left.left):
            x = self.rotate_right(x)
        if self.is_red(x.left) and self.is_red(x.right):
            x = self.flip_colors(x)

        x.count = 1 + _count(x.left) + _count(x.right)
        return x

    def is_red(self, x):
        if x is None:
            return False
        return x.red == 1

    def rotate_left(self, x):
        m = x.right
        x.right = m.left
        m.left = x

        m.red = x.red
        x.red = 1

        x.count = 1 + _count(x.left) + _count(x.right)
        return m

    def rotate_right(self, x):
        m = x.left
        x.left = m.right
        m.right = x

        m.red = x.red
        x.red = 1

        x.count = 1 + _count(x.left) + _count(x.right)
        return m

    def flip_colors(self, x):
        if x.left is not None:
            x.left.red = 0
        if x.right is not None:
            x.right.red = 0
        x.red = 1
        return x

