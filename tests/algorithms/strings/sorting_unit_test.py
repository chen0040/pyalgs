import unittest

from pyalgs.algorithms.strings.sorting import LSD, MSD, String3WayQuickSort
from tests.algorithms.strings.util import words3


class LSDUnitTest(unittest.TestCase):
    def test_lsd(self):
        words = words3()
        print(words)
        LSD.sort(words)
        print(words)

class MSDUnitTest(unittest.TestCase):
    def test_msd(self):
        words = 'more details are provided in the docs for implementation, complexities and further info'.split(' ')
        print(words)
        MSD.sort(words)
        print(words)


class String3WayQuickSortUnitTest(unittest.TestCase):
    def test_msd(self):
        words = 'more details are provided in the docs for implementation, complexities and further info'.split(' ')
        print(words)
        String3WayQuickSort.sort(words)
        print(words)


if __name__ == '__main__':
    unittest.main()