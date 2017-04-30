from pyalgs.algorithms.commons import util
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


class Edge(object):
    v = None
    w = None
    weight = 0

    def __init__(self, v=None, w=None, weight=None):
        if weight is None:
            weight = 0
        self.v = v
        self.w = w
        self.weight = weight

    def start(self):
        return self.v

    def end(self):
        return self.w

    def reverse(self):
        return Edge(self.w, self.v, self.weight)

    def either(self):
        return self.v

    def other(self, v):
        if self.v == v:
            return self.w
        elif self.w == v:
            return self.v
        else:
            raise ValueError('mismatched vertex detected')

    # use for python 2 comparison
    def __cmp__(self, other):
        return util.cmp(self.weight, other.weight)

    # user for python 3 comparison
    def __lt__(self, other):
        return util.less(self.weight, other.weight)

    # user for python 3 comparison
    def __gt__(self, other):
        return util.greater(self.weight, other.weight)

    def __str__(self):
        return str(self.v) + ' =(' + str(self.weight) + ')=> ' + str(self.w)


class EdgeWeightedGraph(object):
    adjList = None
    V = 0

    def __init__(self, vertex_count):
        self.V = vertex_count
        self.adjList = [None] * vertex_count
        for v in range(vertex_count):
            self.adjList[v] = Bag()

    def add_edge(self, edge):
        v = edge.either()
        w = edge.other(v)
        self.adjList[v].add(edge)
        self.adjList[w].add(edge)

    def adj(self, v):
        return self.adjList[v].iterate()

    def vertex_count(self):
        return self.V

    def edges(self):
        for v in range(self.V):
            for e in self.adj(v):
                if e.either() == v:
                    yield e

    def to_graph(self):
        g = Graph()

        for e in self.edges():
            g.add_edge(e.start(), e.end())
        return g

    def to_edge_weighted_digraph(self):
        g = DirectedEdgeWeightedGraph(self.V)

        for e in self.edges():
            g.add_edge(e)
            g.add_edge(e.reverse())
        return g


class DirectedEdgeWeightedGraph(object):
    adjList = None
    V = 0

    def __init__(self, vertex_count):
        self.V = vertex_count
        self.adjList = [None] * vertex_count
        for v in range(vertex_count):
            self.adjList[v] = Bag()

    def add_edge(self, edge):
        v = edge.start()
        self.adjList[v].add(edge)

    def adj(self, v):
        return self.adjList[v].iterate()

    def vertex_count(self):
        return self.V

    def edges(self):
        for v in range(self.V):
            for e in self.adj(v):
                yield e

    def to_graph(self):
        g = Graph()

        for e in self.edges():
            g.add_edge(e.start(), e.end())
        return g

    def to_digraph(self):
        g = Digraph(self.V)

        for e in self.edges():
            g.add_edge(e.start(), e.end())

        return g


class FlowEdge(object):
    v = 0
    w = 0
    capacity = 0
    flow = 0

    def __init__(self, v, w, capacity):
        self.v = v
        self.w = w
        self.capacity = capacity

    def residual_capacity_to(self, end_v):
        if self.w == end_v:
            return self.capacity - self.flow
        elif self.v == end_v:
            return self.flow
        else:
            raise ValueError('end point not belong to flow edge')

    def add_residual_flow_to(self, end_v, delta):
        if self.v == end_v:
            self.flow -= delta
        elif self.w == end_v:
            self.flow += delta
        else:
            raise ValueError('end point not belong to flow edge')

    def start(self):
        return self.v

    def end(self):
        return self.w

    def other(self, x):
        if x == self.v:
            return self.w
        else:
            return self.v

    def __str__(self):
        return str(self.v) + ' =(' + str(self.capacity) + ', ' + str(self.flow) + ')=> ' + str(self.w)


class FlowNetwork(object):

    V = None
    adjList = None

    def __init__(self, V):
        self.V = V
        self.adjList = [None] * V

        for v in range(self.V):
            self.adjList[v] = Bag()

    def adj(self, v):
        return self.adjList[v].iterate()

    def add_edge(self, edge):
        self.adjList[edge.start()].add(edge)
        self.adjList[edge.end()].add(edge)

    def vertex_count(self):
        return self.V

    def edges(self):
        for v in range(self.V):
            for e in self.adjList[v].iterate():
                if e.start() == v:
                    yield e


