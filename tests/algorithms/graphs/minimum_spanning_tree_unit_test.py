import unittest

from pyalgs.algorithms.graphs.minimum_spanning_trees import KruskalMST
from tests.algorithms.graphs.util import create_edge_weighted_graph


class KruskalMSTUnitTest(unittest.TestCase):
    def test_mst(self):
        g = create_edge_weighted_graph()
        mst = KruskalMST(g)

        tree = mst.spanning_tree()

        for e in tree:
            print(e)