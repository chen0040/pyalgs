import unittest

from pyalgs.algorithms.graphs.topological_sort import DepthFirstOrder
from tests.algorithms.graphs.util import create_dag


class DepthFirstOrderUnitTest(unittest.TestCase):

    def test_topological_sort(self):
        G = create_dag()

        topological_sort = DepthFirstOrder(G)

        print(' => '.join([str(i) for i in topological_sort.postOrder()]))


if __name__ == '__main__':
    unittest.main()