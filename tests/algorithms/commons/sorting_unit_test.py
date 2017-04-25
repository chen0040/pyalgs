import unittest

from pyalgs.algorithms.commons.sorting import SelectionSort, InsertionSort, ShellSort, MergeSort, QuickSort, \
    ThreeWayQuickSort


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


class ShellSortTest(unittest.TestCase):
    def test_sort(self):
        a = [4, 2, 1, 23, 4, 5, 6, 7, 8, 9, 20, 11, 13, 34, 66]
        ShellSort.sort(a)
        print(a)
        self.assertEqual(1, a[0])
        self.assertEqual(2, a[1])
        self.assertEqual(4, a[2])


class MergeSortTest(unittest.TestCase):
    def test_sort(self):
        a = [4, 2, 1, 23, 4, 5, 6, 7, 8, 9, 20, 11, 13, 34, 66]
        MergeSort.sort(a)
        print(a)
        self.assertEqual(1, a[0])
        self.assertEqual(2, a[1])
        self.assertEqual(4, a[2])


class QuickSortTest(unittest.TestCase):
    def test_sort(self):
        a = [4, 2, 1, 23, 4, 5, 6, 7, 8, 9, 20, 11, 13, 34, 66]
        QuickSort.sort(a)
        print(a)
        self.assertEqual(1, a[0])
        self.assertEqual(2, a[1])
        self.assertEqual(4, a[2])


class ThreeWayQuickSortTest(unittest.TestCase):
    def test_sort(self):
        a = [4, 2, 1, 23, 4, 5, 6, 7, 8, 9, 20, 11, 13, 34, 66]
        ThreeWayQuickSort.sort(a)
        print(a)
        self.assertEqual(1, a[0])
        self.assertEqual(2, a[1])
        self.assertEqual(4, a[2])


if __name__ == '__main__':
    unittest.main()
