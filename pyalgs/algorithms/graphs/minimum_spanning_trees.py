from abc import ABCMeta, abstractmethod

from pyalgs.algorithms.commons.union_find import UnionFind
from pyalgs.data_structures.commons.bag import Bag
from pyalgs.data_structures.commons.priority_queue import MinPQ


class MST(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def spanning_tree(self):
        pass


class KruskalMST(MST):
    tree = None

    def __init__(self, G):
        minpq = MinPQ.create()
        self.tree = Bag()
        for e in G.edges():
            minpq.enqueue(e)

        uf = UnionFind.create(G.vertex_count())

        while not minpq.is_empty() and self.tree.size() < G.vertex_count() - 1:
            e = minpq.del_min()
            v = e.start()
            w = e.end()
            if not uf.connected(v, w):
                uf.union(v, w)
                self.tree.add(e)

    def spanning_tree(self):
        return self.tree.iterate()
