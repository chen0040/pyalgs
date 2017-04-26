from abc import ABCMeta, abstractmethod

from pyalgs.data_structures.commons.stack import Stack


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
