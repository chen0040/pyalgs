import unittest

from pyalgs.algorithms.commons.union_find import UnionFind, QuickFind


class UnionFindUnitTest(unittest.TestCase):
    def test_find(self):
        uf = UnionFind.create(10)

        uf.union(1, 3)
        uf.union(2, 4)
        uf.union(1, 5)

        self.assertTrue(uf.connected(1, 3))
        self.assertTrue(uf.connected(3, 5))
        self.assertFalse(uf.connected(1, 2))
        self.assertFalse(uf.connected(1, 4))


class QuickFindUnitTest(unittest.TestCase):
    def test_find(self):
        uf = QuickFind(10)

        uf.union(1, 3)
        uf.union(2, 4)
        uf.union(1, 5)

        self.assertTrue(uf.connected(1, 3))
        self.assertTrue(uf.connected(3, 5))
        self.assertFalse(uf.connected(1, 2))
        self.assertFalse(uf.connected(1, 4))

if __name__ == '__main__':
    unittest.main()
