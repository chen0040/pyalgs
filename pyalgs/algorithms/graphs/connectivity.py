from abc import ABCMeta, abstractmethod

from pyalgs.algorithms.graphs.topological_sort import DepthFirstOrder
from pyalgs.data_structures.graphs.graph import EdgeWeightedGraph, Digraph, DirectedEdgeWeightedGraph


class ConnectedComponents(object):
    marked = None
    _id = None
    _count = 0

    def __init__(self, G):
        if isinstance(G, EdgeWeightedGraph):
            G = G.to_graph()

        vertex_count = G.vertex_count()
        self.marked = [False] * vertex_count
        self._id = [-1] * vertex_count
        for v in range(vertex_count):
            if not self.marked[v]:
                self.dfs(G, v)
                self._count += 1

    def dfs(self, G, v):
        self.marked[v] = True
        self._id[v] = self._count
        for w in G.adj(v):
            if not self.marked[w]:
                self.dfs(G, w)

    def connected(self, v, w):
        return self._id[v] == self._id[w]

    def count(self):
        return self._count

    def id(self, v):
        return self._id[v]


class StronglyConnectedComponents(object):
    marked = None
    _id = None
    _count = 0

    def __init__(self, G):
        if isinstance(G, EdgeWeightedGraph):
            raise ValueError('Graph must be directed graph for strongly connected components')
        if isinstance(G, DirectedEdgeWeightedGraph):
            G = G.to_digrah()
        if not isinstance(G, Digraph):
            raise ValueError('Graph must be directed graph for strongly connected components')

        vertex_count = G.vertex_count()
        self.marked = [False] * vertex_count
        self._id = [-1] * vertex_count

        dfo = DepthFirstOrder(G.reverse())
        orders = dfo.postOrder()

        for v in orders:
            if not self.marked[v]:
                self.dfs(G, v)
                self._count += 1

    def dfs(self, G, v):
        self.marked[v] = True
        self._id[v] = self._count
        for w in G.adj(v):
            if not self.marked[w]:
                self.dfs(G, w)

    def connected(self, v, w):
        return self._id[v] == self._id[w]

    def count(self):
        return self._count

    def id(self, v):
        return self._id[v]
