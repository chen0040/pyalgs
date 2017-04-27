import unittest

from pyalgs.algorithms.graphs.shortest_path import DijkstraShortestPath
from tests.algorithms.graphs.util import create_edge_weighted_digraph


class DijkstraShortestPathUnitTest(unittest.TestCase):
    def test_shortest_path(self):
        g = create_edge_weighted_digraph()
        s = 0
        dijkstra = DijkstraShortestPath(g, s)
        for v in range(1, g.vertex_count()):
            if dijkstra.hasPathTo(v):
                print(str(s) + ' is connected to ' + str(v))
                print('shortest path is ' + ' .. '.join([str(i) for i in dijkstra.shortestPathTo(v)]))
                print('path length is ' + str(dijkstra.path_length_to(v)))


if __name__ == '__main__':
    unittest.main()