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
        return QuickFind(size)


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

