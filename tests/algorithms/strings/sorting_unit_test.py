import unittest

from pyalgs.algorithms.strings.sorting import LSD
from tests.algorithms.strings.util import words3


class LSDUnitTest(unittest.TestCase):
    def test_lsd(self):
        words = words3()
        print(words)
        LSD.sort(words)
        print(words)

if __name__ == '__main__':
    unittest.main()