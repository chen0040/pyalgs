from pyalgs.data_structures.commons.queue import Queue


class FordFulkersonMaxFlow(object):
    edgeTo = None
    marked = None
    s = None
    t = None
    value = 0.0
    network = None

    def __init__(self, network, s, t):
        self.s = s
        self.t = t
        self.network = network
        self.value = 0.0
        while self.has_augmenting_path():
            x = self.t
            bottle = float('inf')
            while x != self.s:
                bottle = min(bottle, self.edgeTo[x].residual_capacity_to(x))
                x = self.edgeTo[x].other(x)

            x = self.t
            while x != self.s:
                self.edgeTo[x].add_residual_flow_to(x, bottle)
                x = self.edgeTo[x].other(x)

            self.value += bottle

    def has_augmenting_path(self):
        vertex_count = self.network.vertex_count()
        self.edgeTo = [None] * vertex_count
        self.marked = [False] * vertex_count

        queue = Queue.create()

        queue.enqueue(self.s)
        self.marked[self.s] = True

        while not queue.is_empty():
            x = queue.dequeue()
            for e in self.network.adj(x):
                w = e.other(x)
                if e.residual_capacity(w) > 0:
                    if not self.marked[w]:
                        self.marked[w] = True
                        self.edgeTo[w] = e
                        queue.enqueue(w)

        return self.marked[self.t]

    def max_flow_value(self):
        return self.value

    def min_cut(self):
        queue = Queue.create()
        for edge in self.network.edges():
            if edge.residual_capacity() == 0:
                queue.enqueue(edge)

        return queue.iterate()
