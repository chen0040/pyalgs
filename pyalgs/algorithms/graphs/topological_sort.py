from pyalgs.data_structures.commons.stack import Stack


class DepthFirstOrder(object):

    marked = None
    reversePostOrder = None

    def __init__(self, G):
        self.reversePostOrder = Stack.create()
        vertex_count = G.vertex_count()
        self.marked = [False] * vertex_count

        for v in range(vertex_count):
            if not self.marked[v]:
                self.dfs(G, v)

    def dfs(self, G, v):
        self.marked[v] = True
        for w in G.adj(v):
            if not self.marked[w]:
                self.dfs(G, w)
        self.reversePostOrder.push(v)

    def postOrder(self):
        return self.reversePostOrder.iterate()