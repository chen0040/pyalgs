import unittest

from pyalgs.algorithms.commons.util import less, exchange


class UtilTest(unittest.TestCase):
    def test_less(self):
        self.assertTrue(less(4, 5))
        self.assertFalse(less(4, 4))

    def test_exchange(self):
        a = [2, 4, 5]
        exchange(a, 0, 1)
        self.assertEqual(4, a[0])
        self.assertEqual(2, a[1])

if __name__ == '__main__':
    unittest.main()