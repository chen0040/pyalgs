import unittest

from pyalgs.algorithms.graphs.search import DepthFirstSearch, BreadthFirstSearch
from tests.algorithms.graphs.util import create_graph, create_digraph


class DepthFirstSearchUnitTest(unittest.TestCase):
    def test_dfs(self):
        g = create_graph() # or create_digraph
        s = 0
        dfs = DepthFirstSearch(g, s)

        for v in range(1, g.vertex_count()):
            if dfs.hasPathTo(v):
                print(str(s) + ' is connected to ' + str(v))
                print('path is ' + ' => '.join([str(i) for i in dfs.pathTo(v)]))

    def test_dfs_digraph(self):
        g = create_digraph()
        s = 0
        dfs = DepthFirstSearch(g, s)

        for v in range(1, g.vertex_count()):
            if dfs.hasPathTo(v):
                print(str(s) + ' is connected to ' + str(v))
                print('path is ' + ' => '.join([str(i) for i in dfs.pathTo(v)]))

class BreadthFirstSearchUnitTest(unittest.TestCase):
    def test_dfs(self):
        g = create_graph() # or create_digraph
        s = 0
        dfs = BreadthFirstSearch(g, s)

        for v in range(1, g.vertex_count()):
            if dfs.hasPathTo(v):
                print(str(s) + ' is connected to ' + str(v))
                print('path is ' + ' => '.join([str(i) for i in dfs.pathTo(v)]))

    def test_dfs_digraph(self):
        g = create_digraph()
        s = 0
        dfs = BreadthFirstSearch(g, s)

        for v in range(1, g.vertex_count()):
            if dfs.hasPathTo(v):
                print(str(s) + ' is connected to ' + str(v))
                print('path is ' + ' => '.join([str(i) for i in dfs.pathTo(v)]))


if __name__ == '__main__':
    unittest.main()
