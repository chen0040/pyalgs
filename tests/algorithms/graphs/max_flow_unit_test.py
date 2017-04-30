import unittest

from pyalgs.algorithms.graphs.max_flow import FordFulkersonMaxFlow
from tests.algorithms.graphs.util import create_flow_network


class FordFulkersonMaxFlowUnitTest(unittest.TestCase):
    def test_max_flow(self):
        network = create_flow_network()
        ff = FordFulkersonMaxFlow(network, 0, 7)
        print('max-flow: '+str(ff.max_flow_value()))
        self.assertEqual(28, ff.max_flow_value())

if __name__ == '__main__':
    unittest.main()
