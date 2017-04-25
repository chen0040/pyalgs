import unittest

from pyalgs.algorithms.commons.selecting import BinarySelection
from pyalgs.algorithms.commons.util import is_sorted


class BinarySelectionUnitTest(unittest.TestCase):
    def test_select(self):
        a = [1, 2, 13, 22, 123]
        assert is_sorted(a)
        print(BinarySelection.index_of(a, 13))

if __name__ == '__main__':
    unittest.main()
