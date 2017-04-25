from abc import ABCMeta, abstractmethod


class UnionFind(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def union(self, v, w):
        pass

    @abstractmethod
    def connected(self, v, w):
        pass

    @staticmethod
    def create(size):
        return QuickUnion(size)


class QuickFind(UnionFind):
    id = None

    def __init__(self, capacity):
        self.id = [i for i in range(capacity)]

    def connected(self, v, w):
        return self.id[v] == self.id[w]

    def union(self, v, w):
        p = self.id[v]
        q = self.id[w]

        if p != q:
            for i in range(len(self.id)):
                if self.id[i] == p:
                    self.id[i] = q


class QuickUnion(UnionFind):
    id = None
    sizes = None

    def __init__(self, capacity):
        self.id = [i for i in range(capacity)]
        self.sizes = [1] * capacity

    def root(self, v):
        while v != self.id[v]:
            self.id[v] = self.id[self.id[v]]  # path compression
            v = self.id[v]
        return v

    def connected(self, v, w):
        return self.root(v) == self.root(w)

    def union(self, v, w):
        vroot = self.root(v)
        wroot = self.root(w)

        if self.sizes[vroot] > self.sizes[wroot]:
            self.id[wroot] = vroot
            self.sizes[vroot] += self.sizes[wroot]
        else:
            self.id[vroot] = wroot
            self.sizes[wroot] += self.sizes[vroot]
