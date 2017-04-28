import unittest

from pyalgs.algorithms.graphs.directed_cycle import DirectedCycle
from tests.algorithms.graphs.util import create_dag


class DirectedCycleUnitTest(unittest.TestCase):

    def test_cycle(self):

        dag = create_dag()
        dc = DirectedCycle(dag)

        self.assertFalse(dc.hasCycle())


if __name__ == '__main__':
    unittest.main()