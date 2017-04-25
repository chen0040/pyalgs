import unittest

from pyalgs.data_structures.commons.priority_queue import MinPQ, MaxPQ


class MinPQUnitTest(unittest.TestCase):
    def test_min(self):
        pq = MinPQ.create()
        pq.enqueue(10)
        pq.enqueue(5)
        pq.enqueue(12)
        pq.enqueue(14)
        pq.enqueue(2)

        self.assertFalse(pq.is_empty())
        self.assertEqual(5, pq.size())

        print [i for i in pq.iterate()]

        self.assertEqual(2, pq.del_min())
        self.assertEqual(5, pq.del_min())
        self.assertEqual(10, pq.del_min())
        self.assertEqual(12, pq.del_min())
        self.assertEqual(14, pq.del_min())

        self.assertTrue(pq.is_empty())
        self.assertEqual(0, pq.size())

class MaxPQUnitTest(unittest.TestCase):
    def test_min(self):
        pq = MaxPQ.create()
        pq.enqueue(10)
        pq.enqueue(5)
        pq.enqueue(12)
        pq.enqueue(14)
        pq.enqueue(2)

        self.assertFalse(pq.is_empty())
        self.assertEqual(5, pq.size())

        print [i for i in pq.iterate()]

        self.assertEqual(14, pq.del_max())
        self.assertEqual(12, pq.del_max())
        self.assertEqual(10, pq.del_max())
        self.assertEqual(5, pq.del_max())
        self.assertEqual(2, pq.del_max())

        self.assertTrue(pq.is_empty())
        self.assertEqual(0, pq.size())


if __name__ == '__main__':
    unittest.main()