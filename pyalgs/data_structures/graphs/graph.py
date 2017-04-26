from pyalgs.data_structures.commons.bag import Bag


class Graph(object):
    V = 0
    adjList = None

    def __init__(self, V):
        self.V = V
        self.adjList = [None] * V
        for v in range(V):
            self.adjList[v] = Bag()

    def vertex_count(self):
        return self.V

    def adj(self, v):
        return self.adjList[v].iterate()

    def add_edge(self, v, w):
        self.adjList[v].add(w)
        self.adjList[w].add(v)


class Digraph(object):
    V = 0
    adjList = None

    def __init__(self, V):
        self.V = V
        self.adjList = [None] * V
        for v in range(V):
            self.adjList[v] = Bag()

    def vertex_count(self):
        return self.V

    def adj(self, v):
        return self.adjList[v].iterate()

    def add_edge(self, v, w):
        self.adjList[v].add(w)

    def reverse(self):
        g = Digraph(self.V)
        for v in range(self.V):
            for w in self.adjList[v].iterate():
                g.add_edge(w, v)

        return g
