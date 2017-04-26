import unittest

from pyalgs.data_structures.graphs.graph import Graph, Digraph


class GraphUnitTest(unittest.TestCase):
    def test_graph(self):
        G = Graph(100)

        G.add_edge(1, 2)
        G.add_edge(1, 3)

        print([i for i in G.adj(1)])

        self.assertEqual(100, G.vertex_count())


class DigraphUnitTest(unittest.TestCase):
    def test_digraph(self):
        G = Digraph(100)

        G.add_edge(1, 2)
        G.add_edge(1, 3)

        print([i for i in G.adj(1)])

        self.assertEqual(100, G.vertex_count())

if __name__ == '__main__':
    unittest.main()