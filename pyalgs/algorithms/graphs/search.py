from abc import ABCMeta, abstractmethod

from pyalgs.data_structures.commons.queue import Queue
from pyalgs.data_structures.commons.stack import Stack
from pyalgs.data_structures.graphs.graph import EdgeWeightedGraph


class Paths(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def pathTo(self, v):
        pass

    @abstractmethod
    def hasPathTo(self, v):
        pass


class DepthFirstSearch(Paths):
    marked = None
    edgesTo = None
    s = None

    def __init__(self, G, s):
        if isinstance(G, EdgeWeightedGraph):
            G = G.to_graph()
        self.s = s
        vertex_count = G.vertex_count()
        self.marked = [False] * vertex_count
        self.edgesTo = [-1] * vertex_count
        self.dfs(G, s)

    def dfs(self, G, v):
        self.marked[v] = True
        for w in G.adj(v):
            if not self.marked[w]:
                self.edgesTo[w] = v
                self.dfs(G, w)

    def hasPathTo(self, v):
        return self.marked[v]

    def pathTo(self, v):
        x = v
        path = Stack.create()
        while x != self.s:
            path.push(x)
            x = self.edgesTo[x]
        path.push(self.s)
        return path.iterate()


class BreadthFirstSearch(Paths):

    marked = None
    s = None
    edgeTo = None

    def __init__(self, G, s):
        if isinstance(G, EdgeWeightedGraph):
            G = G.to_graph()
        self.s = s
        vertex_count = G.vertex_count()
        self.marked = [False] * vertex_count
        self.edgeTo = [-1] * vertex_count

        queue = Queue.create()

        queue.enqueue(s)
        while not queue.is_empty():
            v = queue.dequeue()
            self.marked[v] = True
            for w in G.adj(v):
                if not self.marked[w]:
                    self.edgeTo[w] = v
                    queue.enqueue(w)

    def hasPathTo(self, v):
        return self.marked[v]

    def pathTo(self, v):
        x = v
        path = Stack.create()
        while x != self.s:
            path.push(x)
            x = self.edgeTo[x]
        path.push(self.s)
        return path.iterate()