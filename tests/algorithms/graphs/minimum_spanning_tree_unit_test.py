import unittest

from pyalgs.algorithms.graphs.minimum_spanning_trees import KruskalMST, LazyPrimMST, EagerPrimMST
from tests.algorithms.graphs.util import create_edge_weighted_graph


class KruskalMSTUnitTest(unittest.TestCase):
    def test_mst(self):
        g = create_edge_weighted_graph()
        mst = KruskalMST(g)

        tree = mst.spanning_tree()

        for e in tree:
            print(e)


class LazyPrimMSTUnitTest(unittest.TestCase):
    def test_mst(self):
        g = create_edge_weighted_graph()
        mst = LazyPrimMST(g)

        tree = mst.spanning_tree()

        for e in tree:
            print(e)


class EagerPrimMSTUnitTest(unittest.TestCase):
    def test_mst(self):
        g = create_edge_weighted_graph()
        mst = EagerPrimMST(g)

        tree = mst.spanning_tree()

        for e in tree:
            print(e)


if __name__ == '__main__':
    unittest.main()
