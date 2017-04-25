import unittest

from pyalgs.algorithms.commons.sorting import SelectionSort, InsertionSort


class SelectionSortTest(unittest.TestCase):

    def test_sort(self):
        a = [4, 2, 1]
        SelectionSort.sort(a)
        self.assertEqual(1, a[0])
        self.assertEqual(2, a[1])
        self.assertEqual(4, a[2])

class InsertionSortTest(unittest.TestCase):

    def test_sort(self):
        a = [4, 2, 1]
        InsertionSort.sort(a)
        self.assertEqual(1, a[0])
        self.assertEqual(2, a[1])
        self.assertEqual(4, a[2])

if __name__ == '__main__':
    unittest.main()