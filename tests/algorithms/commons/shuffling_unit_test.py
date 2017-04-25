import unittest

from pyalgs.algorithms.commons.shuffling import KnuthShuffle


class KnuthShuffleUnitTest(unittest.TestCase):
    def test_shuffle(self):
        a = [1, 2, 13, 22, 123]
        KnuthShuffle.shuffle(a)
        print(a)

if __name__ == '__main__':
    unittest.main()