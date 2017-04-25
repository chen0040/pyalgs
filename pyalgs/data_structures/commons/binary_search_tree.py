from abc import ABCMeta, abstractmethod


class Node(object):
    key = None
    value = None

    left = None
    right = None

    count = 0

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.count = 1


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

    @staticmethod
    def create():
        return BinarySearchTree()
