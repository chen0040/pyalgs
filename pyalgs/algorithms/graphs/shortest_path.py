from abc import ABCMeta, abstractmethod

from pyalgs.algorithms.commons import util
from pyalgs.algorithms.graphs.topological_sort import DepthFirstOrder
from pyalgs.data_structures.commons.priority_queue import IndexMinPQ
from pyalgs.data_structures.commons.stack import Stack
from pyalgs.data_structures.graphs.graph import Digraph, Graph, EdgeWeightedGraph


class ShortestPath(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def shortestPathTo(self, v):
        pass

    @abstractmethod
    def hasPathTo(self, v):
        pass

    @abstractmethod
    def path_length_to(self, v):
        pass


class DijkstraShortestPath(ShortestPath):
    edgeTo = None
    s = 0
    pq = None
    cost = None

    def __init__(self, G, s):
        if isinstance(G, Graph):
            raise ValueError('Graph must be edge weighted')
        if isinstance(G, Digraph):
            raise ValueError('Graph must be edge weighted')
        if isinstance(G, EdgeWeightedGraph):
            G = G.to_edge_weighted_digraph()

        vertex_count = G.vertex_count()
        self.pq = IndexMinPQ(vertex_count)
        self.s = s

        self.marked = [False] * vertex_count
        self.edgeTo = [None] * vertex_count
        self.cost = [float("inf")] * vertex_count

        self.cost[s] = 0
        self.pq.insert(s, 0.0)

        while not self.pq.is_empty():
            v = self.pq.del_min()
            self.marked[v] = True
            for e in G.adj(v):
                self.relax(e)

    def relax(self, e):
        v = e.start()
        w = e.end()
        if self.cost[w] > self.cost[v] + e.weight:
            self.cost[w] = self.cost[v] + e.weight
            self.edgeTo[w] = e
            if self.pq.contains_index(w):
                self.pq.decrease_key(w, self.cost[w])
            else:
                self.pq.insert(w, self.cost[w])

    def hasPathTo(self, v):
        return self.marked[v]

    def shortestPathTo(self, v):
        path = Stack.create()
        x = v
        while x != self.s:
            path.push(self.edgeTo[x])
            x = self.edgeTo[x].start()

        return path.iterate()

    def path_length_to(self, v):
        return self.cost[v]


class TopologicalSortShortestPath(ShortestPath):
    marked = None
    edgeTo = None
    cost = None
    s = 0

    def __init__(self, G, s):
        vertex_count = G.vertex_count()
        self.marked = [False] * vertex_count
        self.edgeTo = [None] * vertex_count
        self.cost = [float('inf')] * vertex_count
        self.s = s

        dfo = DepthFirstOrder(G)
        orders = dfo.postOrder()

        self.cost[s] = 0

        for v in orders:
            for e in G.adj(v):
                self.relax(e)

    def relax(self, e):
        v = e.start()
        w = e.end()
        if self.cost[w] > self.cost[v] + e.weight:
            self.cost[w] = self.cost[v] + e.weight
            self.edgeTo[w] = e
            self.marked[w] = True

    def shortestPathTo(self, v):
        path = Stack.create()
        x = v
        while x != self.s:
            path.push(self.edgeTo[x])
            x = self.edgeTo[x].start()

        return path.iterate()

    def hasPathTo(self, v):
        return self.marked[v]

    def path_length_to(self, v):
        return self.cost[v]


class BellmanFordShortestPath(ShortestPath):

    s = None
    edgeTo = None
    cost = None
    negativeDirectedCycle = False
    vertexCount = 0

    def __init__(self, G, s):
        self.vertexCount = G.vertex_count()
        self.cost = [float('inf')] * self.vertexCount
        self.edgeTo = [None] * self.vertexCount

        self.cost[s] = 0
        self.s = s

        for i in range(self.vertexCount):
            for v in range(self.vertexCount):
                for e in G.adj(v):
                    self.relax(e)

        for v in range(self.vertexCount):
            for e in G.adj(v):
                if self.relax(e):
                    self.negativeDirectedCycle = True

    def relax(self, e):
        v = e.start()
        w = e.end()

        if self.cost[w] > self.cost[v] + e.weight:
            self.cost[w] = self.cost[v] + e.weight
            self.edgeTo[w] = e
            return True
        return False

    def hasNegativeDirectedCycle(self):
        return self.negativeDirectedCycle

    def shortestPathTo(self, v):
        path = Stack.create()
        x = v
        counter = 0
        while x != self.s:
            path.push(self.edgeTo[x])
            if self.edgeTo[x] is None:
                return None
            x = self.edgeTo[x].start()
            counter += 1
            if counter > self.vertexCount:
                return None

        return path.iterate()

    def hasPathTo(self, v):
        return self.shortestPathTo(v) is not None

    def path_length_to(self, v):
        return self.cost[v]
