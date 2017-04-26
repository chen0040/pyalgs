import unittest
from random import randint

from pyalgs.algorithms.graphs.connectivity import ConnectedComponents
from tests.algorithms.graphs.util import create_graph_4_connected_components


class ConnectedComponentsUnitTest(unittest.TestCase):
    def test_cc(self):
        G = create_graph_4_connected_components()

        cc = ConnectedComponents(G)
        print('connected component count: ' + str(cc.count()))

        self.assertEqual(3, cc.count())

        for v in range(G.vertex_count()):
            print('id[' + str(v) + ']: ' + str(cc.id(v)))
        for v in range(G.vertex_count()):
            r = randint(0, G.vertex_count()-1)
            if cc.connected(v, r):
                print(str(v) + ' is connected to ' + str(r))


if __name__ == '__main__':
    unittest.main()
