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


class LazyPrimMST(MST):
    tree = None
    marked = None
    minpq = None

    def __init__(self, G):
        self.minpq = MinPQ.create()
        self.tree = Bag()
        vertex_count = G.vertex_count()
        self.marked = [False] * vertex_count
        self.visit(G, 0)

        while not self.minpq.is_empty() and self.tree.size() < vertex_count-1:
            edge = self.minpq.del_min()
            v = edge.start()
            w = edge.end()
            if self.marked[v] and self.marked[w]:
                continue
            self.tree.add(edge)
            if not self.marked[v]:
                self.visit(G, v)
            if not self.marked[w]:
                self.visit(G, w)

    def visit(self, G, v):
        self.marked[v] = True
        for e in G.adj(v):
            w = e.other(v)
            if not self.marked[w]:
                self.minpq.enqueue(e)

    def spanning_tree(self):
        return self.tree.iterate()

