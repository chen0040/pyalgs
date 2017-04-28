from pyalgs.data_structures.commons.stack import Stack
from pyalgs.data_structures.graphs.graph import DirectedEdgeWeightedGraph, Digraph


class DirectedCycle(object):

    marked = None
    onStack = None
    cycle = None
    edgeTo = None

    def __init__(self, G):
        if isinstance(G, DirectedEdgeWeightedGraph):
            G = G.to_digraph()

        if not isinstance(G, Digraph):
            raise ValueError('Graph must be unweighted digraph')

        vertex_count = G.vertex_count()
        self.marked = [False] * vertex_count
        self.onStack = [False] * vertex_count
        self.edgeTo = [-1] * vertex_count

        for v in range(vertex_count):
            if not self.marked[v]:
                self.dfs(G, v)

    def dfs(self, G, v):
        self.marked[v] = True
        self.onStack[v] = True

        for w in G.adj(v):
            if not self.marked[w]:
                self.edgeTo[w] = v
                self.dfs(G, w)
            elif self.cycle is not None:
                break
            elif self.onStack[w]:
                self.cycle = Stack.create()
                x = v
                while x != w:
                    self.cycle.push(x)
                    x = self.edgeTo[x]
                self.cycle.push(w)
                self.cycle.push(v)
                break

        self.onStack[v] = False

    def hasCycle(self):
        return self.cycle is not None

    def get_cycle(self):
        return self.cycle.iterate()
